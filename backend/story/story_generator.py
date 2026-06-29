# backend/story/story_generator.py

import json
from llm.ollama_client import OllamaClient


class StoryGenerator:

    def __init__(self):
        self.llm = OllamaClient()


    def generate_story(self, raw_text):

        prompt = f"""

You are an expert storyboard creator for educational animations.

Convert the government procedure into a natural animated story.

RULES:

1. Automatically choose a suitable main character based on the document context.

Examples:

- Defence pension → Colonel Sharma
- Senior citizen pension → Mr Verma
- Farmer scheme → Farmer Ramesh
- Student scholarship → Priya
- Health service → Anita
- General citizen service → Rajesh

Do not use these examples literally every time.
Choose a character intelligently based on the uploaded document.

Keep the same character throughout the story.


2. Number of scenes should NOT be fixed.

Scene count should depend on:

- complexity of process
- number of steps
- document length

Guidelines:

Simple process:
3–5 scenes

Medium process:
6–8 scenes

Complex process:
8–15 scenes


3. Story structure:

Beginning:
- introduce character
- show problem

Middle:
- learning/discovery
- process journey

Ending:
- successful completion
- positive outcome


4. Each scene MUST contain:

{{
"scene":1,
"visual":"screen visuals",
"narration":"full narration"
}}


5. Narration should be natural and conversational.

BAD:

"User opens website."

GOOD:

"Rajesh opened his phone and carefully visited the website to begin the application process."


6. Visual should describe animation clearly.

Example:

"visual":
"Rajesh sitting at home using mobile phone while notification appears."


7. Keep continuity between scenes.

8. Keep language simple for senior citizens and people with low digital literacy.

9. Return ONLY valid JSON.


Government document:

{raw_text}


Return:

{{
"story":[]
}}

"""

        print("\nSending request to Ollama...", flush=True)

        response = self.llm.generate(prompt)

        raw_output = response

        print("\n====== RAW STORY ======")
        print(raw_output)
        print("=======================\n")

        try:

            # remove markdown if model adds it
            cleaned = raw_output.replace(
                "```json",
                ""
            ).replace(
                "```",
                ""
            )

            story_json = json.loads(
                cleaned
            )

            return story_json

        except Exception as e:

            print(
                "Story parsing error:",
                e
            )

            return {

                "story":[

                    {
                        "scene":1,

                        "visual":"Colonel Sharma sitting at home",

                        "narration":"Colonel Sharma received an important notification regarding his Life Certificate."
                    }

                ]
            }