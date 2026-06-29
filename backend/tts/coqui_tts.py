# backend/tts/coqui_tts.py
# FAST TESTING VERSION using gTTS (Google Text-to-Speech)

import os
from gtts import gTTS

class CoquiTTSClient:
    def __init__(self):
        pass # No heavy models to load!

    def generate_audio(self, hindi_text: str, output_path: str) -> str:
        """Generates a FAST audio file from Hindi text using Google TTS."""
        os.makedirs(os.path.dirname(output_path), exist_ok=True)
        
        print(f"Generating audio via gTTS for: {hindi_text[:50]}...")
        
        # Use gTTS for instant generation (requires internet)
        tts = gTTS(text=hindi_text, lang='hi', slow=False)
        # gTTS saves as MP3, so ensure the extension is .mp3 regardless of what was passed
        output_path = output_path.replace(".wav", ".mp3")
        tts.save(output_path)
        
        print(f"Audio saved to: {output_path}")
        return output_path