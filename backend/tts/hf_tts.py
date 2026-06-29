# backend/tts/hf_tts.py

import os
import torch
import scipy.io.wavfile as wavfile
from transformers import VitsModel, AutoTokenizer

class HFTTSClient:
    def __init__(self):
        self.model_name = "facebook/mms-tts-hin"
        self.model = None
        self.tokenizer = None
        self.device = "cuda" if torch.cuda.is_available() else "cpu"

    def _load_model(self):
        if self.model is None:
            print("Loading HuggingFace TTS model... (This may take a few minutes on the first run)", flush=True)
            self.tokenizer = AutoTokenizer.from_pretrained(self.model_name)
            self.model = VitsModel.from_pretrained(self.model_name)
            self.model.to(self.device)
            print("HuggingFace TTS model loaded successfully!", flush=True)

    def generate_audio(self, hindi_text: str, output_path: str) -> str:
        self._load_model()
        
        os.makedirs(os.path.dirname(output_path), exist_ok=True)
        
        print(f"Generating audio for: {hindi_text[:50]}...", flush=True)
        
        inputs = self.tokenizer(hindi_text, return_tensors="pt").to(self.device)
        
        with torch.no_grad():
            output = self.model(**inputs).waveform
        
        # The model outputs a tensor. We need to convert it to a numpy array for scipy.
        # It's typically in 16kHz or 24kHz depending on the model.
        waveform_np = output.cpu().numpy().squeeze()
        sample_rate = self.model.config.sampling_rate
        
        wavfile.write(output_path, rate=sample_rate, data=waveform_np)
        
        print(f"Audio saved to: {output_path}", flush=True)
        return output_path