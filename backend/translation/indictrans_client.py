# backend/translation/indictrans_client.py

import torch
from transformers import AutoModelForSeq2SeqLM, AutoTokenizer

class IndicTransClient:
    def __init__(self):
        self.model_name = "Helsinki-NLP/opus-mt-en-hi"
        self.tokenizer = None
        self.model = None
        self.device = "cuda" if torch.cuda.is_available() else "cpu"

    def _load_model(self):
        if self.model is None:
            print("Loading Translation model... (This may take a few minutes on the first run)", flush=True)
            self.tokenizer = AutoTokenizer.from_pretrained(self.model_name)
            self.model = AutoModelForSeq2SeqLM.from_pretrained(self.model_name)
            self.model.to(self.device)
            self.model.eval()
            print("Translation model loaded successfully!", flush=True)

    def translate_to_hindi(self, english_text: str) -> str:
        self._load_model()
        
        inputs = self.tokenizer(
            english_text, 
            return_tensors="pt", 
            padding=True, 
            truncation=True, 
            max_length=256
        ).to(self.device)
        
        with torch.no_grad():
            generated_tokens = self.model.generate(
                **inputs,
                max_length=256,
                num_beams=5,
                early_stopping=True
            )
        
        hindi_text = self.tokenizer.batch_decode(generated_tokens, skip_special_tokens=True)[0]
        return hindi_text