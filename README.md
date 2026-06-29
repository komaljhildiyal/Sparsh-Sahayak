<<<<<<< HEAD
# 🇮🇳 SPARSH Life Certificate Tutorial System

An intelligent, multilingual application that takes SPARSH government procedure text as input, converts it into simple animated video tutorials, narrates instructions in Hindi, works offline, and has a senior-citizen friendly UI.

> 🎯 **Target Users:** Senior defence pensioners (70+ years) in Uttarakhand, India.

---

## ✨ Features

| Feature | Description |
|---|---|
| **AI Simplification** | Uses LLaMA 3 (via Ollama) to break down complex government jargon into simple, bite-sized steps. |
| **Hindi Translation** | Automatically translates English procedures into Hindi using HuggingFace AI models. |
| **Realistic Voiceover** | Generates natural-sounding Hindi voice narration using Facebook MMS-TTS. |
| **Video Generation** | Automatically creates high-contrast, large-text video slides and stitches them with audio using FFmpeg. |
| **Senior-Friendly UI** | Extra-large buttons, high-contrast colors, and a built-in browser voice guide for the visually impaired. |
| **100% Offline & Free** | Runs entirely locally. No paid APIs, no data leaves the machine. |

---

## 🛠️ Tech Stack

| Layer | Technology |
|---|---|
| **LLM** | Ollama with LLaMA 3 (running locally) |
| **Translation** | HuggingFace (`Helsinki-NLP/opus-mt-en-hi`) |
| **Voice TTS** | HuggingFace (`facebook/mms-tts-hin`) |
| **Visuals** | Pillow (Python Image Library) |
| **Video Merge** | FFmpeg (via `ffmpeg-python`) |
| **Backend** | FastAPI (Python) — Uses Multiprocessing for deadlock-proof background tasks |
| **Frontend** | React.js |
| **Database** | SQLite (fully local, free) |

---

## 📋 Prerequisites

Before you begin, ensure you have the following installed on your Windows machine:

- **Python 3.11+**
- **Node.js & npm**
- **Ollama** installed and running with LLaMA 3 downloaded.
  - Download Ollama from [ollama.com](https://ollama.com)
  - Open a terminal and run: `ollama run llama3`
- **FFmpeg** installed and added to your Windows PATH.
  - Download from [gyan.dev](https://gyan.dev) *(Get the essentials build)*
  - Extract it and add the `bin` folder to your System Environment Variables PATH.
- **Hindi Font:**
  - Download `NotoSansDevanagari-Regular.ttf` from [Google Fonts](https://fonts.google.com)
  - Create a `fonts` folder inside `backend/` and place the `.ttf` file there.

---

## 🚀 Setup & Installation

### 1. Backend Setup

Open a terminal, navigate to the `backend` folder, and install the Python dependencies:

```bash
cd backend
pip install -r requirements.txt
```

### 2. Frontend Setup

Open a second terminal, navigate to the `frontend` folder, and install the Node modules:

```bash
cd frontend
npm install
```

---

## 🏃‍♂️ How to Run

You need **three things running simultaneously** for the app to work.

### 1. Start Ollama *(if not already running in background)*

```bash
ollama serve
```

> Or just open the Ollama desktop app.

### 2. Start the Backend

Open a terminal, navigate to `backend`, and start the FastAPI server. We use `python -u` to ensure logs print instantly on Windows:

```bash
cd backend
python -u -m uvicorn main:app --port 8001
```

> We use port `8001` to avoid Windows port `8000` conflicts. If port `8000` is free, you can use that.

### 3. Start the Frontend

Open a third terminal, navigate to `frontend`, and start the React app:

```bash
cd frontend
npm start
```

The app will automatically open in your browser at **http://localhost:3000**.

> ⚠️ **Important:** If you run the backend on port `8001`, make sure your React files (`TopicSelect.js` and `VideoPlayer.js`) are pointing to `http://localhost:8001/api/...`.

---

## 🎬 How to Use

1. Open **http://localhost:3000** in your browser.
2. Click the big orange **"शुरू करें (Start)"** button.
3. Paste any SPARSH pension procedure text in English into the text box.
4. Click **"वीडियो बनाएं (Create Video)"**.
5. Wait **1–3 minutes** while the AI pipeline processes the text, translates it, generates the voiceover, and creates the video.
6. The video will automatically play when ready!

---

## ⚠️ Troubleshooting (Windows Specific)

### 1. Port 8000 is already in use (`Errno 10048`)

Windows often holds onto ports. Either kill the process using the PID:

```bash
netstat -ano | findstr :8000
taskkill /PID <PID> /F
```

Or simply run the backend on a different port:

```bash
python -u -m uvicorn main:app --port 8001
```

### 2. Hindi text appears as empty boxes in the video

This means Pillow couldn't find a Hindi font. Ensure you have downloaded `NotoSansDevanagari-Regular.ttf` and placed it inside `backend/fonts/`. Verify the path in `text_image_generator.py` matches your exact file name.

### 3. Backend terminal freezes when generating video

This was fixed by using Python's `multiprocessing.Process` instead of FastAPI's `BackgroundTasks`. Ensure your `main.py` uses:

```python
from multiprocessing import Process
```

...and starts the pipeline via `p = Process(...)`. Also, always run Uvicorn with the `python -u` flag for unbuffered logging.

### 4. FFmpeg not found error

Ensure FFmpeg is installed and the `bin` folder is added to your Windows PATH. You **must restart your terminal** after adding it to PATH for it to take effect.
=======
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
