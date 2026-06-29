# backend/llm/ollama_client.py

import ollama
import json
import re
from llm.prompts import SYSTEM_PROMPT, EXTRACT_STEPS_PROMPT

class OllamaClient:
    def __init__(self, model_name="llama3"):
        self.model_name = model_name

    def check_connection(self):
        try:
            ollama.generate(model=self.model_name, prompt="Hi")
            return True
        except Exception as e:
            print(f"Ollama connection error: {e}", flush=True)
            return False

    def extract_steps_from_text(self, raw_text):
        user_prompt = EXTRACT_STEPS_PROMPT.format(text=raw_text)
        
        try:
            response = ollama.chat(
                model=self.model_name,
                messages=[
                    {'role': 'system', 'content': SYSTEM_PROMPT},
                    {'role': 'user', 'content': user_prompt}
                ],
                format='json'
            )
            
            raw_response = response['message']['content']
            print(f"DEBUG LLM Raw Output: {raw_response}", flush=True)
            
            parsed_json = json.loads(raw_response)
            
            if isinstance(parsed_json, dict) and 'steps' in parsed_json:
                return parsed_json['steps']
            elif isinstance(parsed_json, list):
                return parsed_json
            else:
                print("LLM returned JSON, but not in the expected format.", flush=True)
                return []

        except json.JSONDecodeError as e:
            print(f"Failed to parse LLM response into JSON: {e}", flush=True)
            return []
        except Exception as e:
            print(f"Error generating text with Ollama: {e}", flush=True)
            return []

    def generate_story(self, raw_text):

        prompt = f"""
    You are creating an educational animated story for senior citizens.

    Convert the following government procedure into a natural story.

    Rules:

    1. Main character must always be:
    Colonel Sharma, retired defence officer.

    2. Story must have:

    - Problem introduction
    - Learning process
    - Step-by-step journey
    - Success ending
    - Emotional flow

    3. Create 8–10 scenes.

    4. Each scene must contain:

    {{
    "scene":1,
    "visual":"what should appear on screen",
    "narration":"full narration sentence"
    }}

    5. Narration should be conversational and easy for elderly users.

    6. Do NOT summarize.

    7. Do NOT write:
    "Colonel Sharma clicked button"

    Instead write:

    "Colonel Sharma was worried because his Life Certificate was due. He wondered if he would need to travel again and stand in long queues."

    Government procedure:

    {raw_text}

    Return only JSON:

    {{
    "story":[]
    }}

    """

        response = ollama.generate(
            model="llama3",
            prompt=prompt
        )

        return response["response"]
    def generate(self, prompt):

        import requests

        response = requests.post(

            "http://localhost:11434/api/generate",

            json={

                "model":"llama3",
                "prompt":prompt,
                "stream":False
            }

        )

        data = response.json()

        return data["response"]