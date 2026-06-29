# SparshSahayak – AI-Powered Government Procedure Tutorial Generator

SparshSahayak is an intelligent system designed to simplify complex government procedures for senior citizens and defence pensioners. It automatically transforms text documents and official instructions into easy-to-understand animated story-based tutorials with voice guidance.

The project focuses on improving accessibility for users with limited digital literacy, especially retired defence personnel living in remote and hilly regions.

## Problem Statement

Defence pensioners are required to submit annual Life Certificates through the SPARSH portal. Many senior citizens face difficulties understanding digital systems and navigating complex interfaces.

SparshSahayak addresses this challenge by converting difficult procedural content into:

- Story-based visual explanations
- Animated tutorials
- Voice-guided instructions
- Step-by-step process demonstrations

## Features

- Upload government documents (PDF/Text)
- Automatic document text extraction
- AI-generated procedural storytelling
- Dynamic scene generation
- Hindi translation support
- Hindi text-to-speech narration
- Animated tutorial video creation
- User-friendly interface for senior citizens

## Tech Stack

### Backend
- FastAPI
- SQLite
- Ollama (LLM)
- Hugging Face TTS
- FFmpeg
- Python

### Frontend
- React.js
- HTML/CSS

## Prerequisites
Before you begin, ensure you have the following installed on your Windows machine:

- Python 3.11+
- Node.js & npm
- Ollama installed and running with LLaMA 3 downloaded.
          - Download Ollama from ollama.com
          - Open a terminal and run: ollama run llama3
- FFmpeg installed and added to your Windows PATH.
          - Download from gyan.dev (Get the essentials build)
          - Extract it and add the bin folder to your System Environment Variables PATH.
-Hindi Font:
          - Download NotoSansDevanagari-Regular.ttf from Google Fonts
          - Create a fonts folder inside backend/ and place the .ttf file there.

## Workflow

Document Upload  
↓  
Text Extraction  
↓  
AI Story Generation  
↓  
Scene Creation  
↓  
Translation (English → Hindi)  
↓  
Voice Generation  
↓  
Animation Generation  
↓  
Final Tutorial Video Output

## Installation

### Clone repository

git clone <repo-link>

cd sparsh-tutorial-main

### Backend setup

cd backend

pip install -r requirements.txt

python -u -m uvicorn main:app --port 8001

### Frontend setup

cd frontend

npm install

npm start

## Target Users

- Defence Pensioners
- Senior Citizens
- Digitally inexperienced users
- Citizens in remote and rural areas

## Future Improvements

- Multiple regional language support
- Interactive chatbot assistant
- Face/avatar-based narration

## Project Goal

To make government services understandable and accessible for everyone through AI-powered visual learning.
>>>>>>> e8967f60fa8f3d4c684ce732745562466873e7c5
