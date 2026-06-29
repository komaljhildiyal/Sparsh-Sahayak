# backend/main.py

from fastapi import FastAPI, HTTPException
from fastapi.responses import FileResponse
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import os
import traceback
from fastapi import UploadFile,File
import shutil
from parser.document_parser import DocumentParser
from multiprocessing import Process

# Import our custom modules
from database.db import init_db, get_db_connection
from llm.ollama_client import OllamaClient
from translation.indictrans_client import IndicTransClient
from tts.hf_tts import HFTTSClient # Using HuggingFace TTS now!
from animation.scene_generator import SceneGenerator
from animation.video_stitcher import VideoStitcher
from story.story_generator import StoryGenerator

# --- App Initialization ---
app = FastAPI(title="SPARSH Tutorial System", version="1.0")

# --- CORS Configuration ---
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

MEDIA_DIR = os.path.join(os.path.dirname(__file__), "media")

@app.on_event("startup")
async def startup_event():
    init_db()
    os.makedirs(MEDIA_DIR, exist_ok=True)
    print("🚀 SPARSH Tutorial System Backend Started!", flush=True)

class TutorialRequest(BaseModel):
    topic: str
    text: str

# --- The Core Pipeline ---
def process_tutorial_pipeline(tutorial_id: int, raw_text: str):

    conn = get_db_connection()

    try:

        conn.execute(
            "UPDATE tutorials SET status = ? WHERE id = ?",
            ("processing", tutorial_id)
        )

        conn.commit()


        # ===========================
        # STORY GENERATION
        # ===========================

        print(
            f"[Tutorial {tutorial_id}] Step 1: Generating story...",
            flush=True
        )

        story_generator = StoryGenerator()

        story_data = story_generator.generate_story(
            raw_text
        )


        steps_data = []

        for scene in story_data["story"]:

            steps_data.append(
                {
                    "step_number":
                    scene["scene"],

                    "english_text":
                    scene["narration"]
                }
            )


        if not steps_data:

            raise ValueError(
                "Story generation failed"
            )


        # ===========================
        # SAVE STEPS TO DATABASE
        # ===========================

        for step in steps_data:

            conn.execute(
                """
                INSERT INTO steps
                (
                tutorial_id,
                step_number,
                english_text
                )
                VALUES
                (
                ?,?,?
                )
                """,

                (
                    tutorial_id,
                    step["step_number"],
                    step["english_text"]
                )
            )

        conn.commit()


        translator = IndicTransClient()

        tts_client = HFTTSClient()

        scene_gen = SceneGenerator()


        db_steps = conn.execute(
            """
            SELECT *
            FROM steps
            WHERE tutorial_id=?
            ORDER BY step_number
            """,
            (tutorial_id,)
        ).fetchall()


        tutorial_dir = os.path.join(
            MEDIA_DIR,
            str(tutorial_id)
        )


        processed_steps_data = []


        for step in db_steps:

            step_dict = dict(step)

            step_num = step_dict[
                "step_number"
            ]

            english_text = step_dict[
                "english_text"
            ]


            print(
                f"[Tutorial {tutorial_id}] Step {step_num}: Translating...",
                flush=True
            )

            hindi_text = (
                translator.translate_to_hindi(
                    english_text
                )
            )


            print(
                f"[Tutorial {tutorial_id}] Step {step_num}: Generating voice...",
                flush=True
            )


            audio_filename = (
                f"step_{step_num}.wav"
            )

            audio_path = os.path.join(
                tutorial_dir,
                "audio",
                audio_filename
            )


            actual_audio_path = (
                tts_client.generate_audio(
                    hindi_text,
                    audio_path
                )
            )


            conn.execute(
                """
                UPDATE steps
                SET
                hindi_text=?,
                audio_path=?
                WHERE id=?
                """,

                (
                    hindi_text,
                    actual_audio_path,
                    step_dict["id"]
                )
            )

            conn.commit()


            step_dict[
                "hindi_text"
            ] = hindi_text


            step_dict[
                "audio_path"
            ] = actual_audio_path


            print(
                f"[Tutorial {tutorial_id}] Step {step_num}: Generating scene...",
                flush=True
            )


            updated_step_dict = (
                scene_gen.generate_step_video(
                    step_dict,
                    tutorial_id,
                    tutorial_dir
                )
            )


            conn.execute(
                """
                UPDATE steps
                SET
                image_path=?,
                scene_video_path=?
                WHERE id=?
                """,

                (
                    updated_step_dict[
                        "image_path"
                    ],

                    updated_step_dict[
                        "scene_video_path"
                    ],

                    step_dict["id"]
                )
            )

            conn.commit()


            processed_steps_data.append(
                updated_step_dict
            )


        print(
            f"[Tutorial {tutorial_id}] Step 3: Stitching video...",
            flush=True
        )


        stitcher = VideoStitcher()


        final_video_path = (
            stitcher.create_final_video(
                processed_steps_data,
                tutorial_id,
                tutorial_dir
            )
        )


        conn.execute(
            """
            UPDATE tutorials
            SET
            status=?,
            final_video_path=?
            WHERE id=?
            """,

            (
                "completed",
                final_video_path,
                tutorial_id
            )
        )

        conn.commit()


        print(
            f"[Tutorial {tutorial_id}] ✅ Pipeline Complete!",
            flush=True
        )


    except Exception as e:

        print(
            f"[Tutorial {tutorial_id}] ❌ Pipeline Failed: {e}",
            flush=True
        )

        traceback.print_exc()

        conn.execute(
            """
            UPDATE tutorials
            SET status=?
            WHERE id=?
            """,
            (
                "failed",
                tutorial_id
            )
        )

        conn.commit()


    finally:

        conn.close()

# --- API Endpoints ---

@app.post("/api/tutorials")
async def create_tutorial(
    topic: str = "",
    text: str = "",
    file: UploadFile = File(None)
):

    tutorial_text = text


    # If user uploads a file
    if file:

        file_location = f"uploads/{file.filename}"

        with open(file_location, "wb") as buffer:

            shutil.copyfileobj(
                file.file,
                buffer
            )

        parser = DocumentParser()

        tutorial_text = parser.parse_document(
            file_location
        )

        print("\n========== EXTRACTED TEXT ==========")
        print(tutorial_text)
        print("====================================")


    conn = get_db_connection()

    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO tutorials (topic, status) VALUES (?, ?)",
        (topic, "pending")
    )

    conn.commit()

    tutorial_id = cursor.lastrowid

    conn.close()


    # Start pipeline process
    p = Process(
        target=process_tutorial_pipeline,
        args=(
            tutorial_id,
            tutorial_text
        )
    )

    p.start()


    return {
        "message": "Tutorial generation started!",
        "tutorial_id": tutorial_id,
        "status": "pending"
    }

@app.get("/api/tutorials/{tutorial_id}")
async def get_tutorial_status(tutorial_id: int):
    conn = get_db_connection()
    tutorial = conn.execute("SELECT * FROM tutorials WHERE id = ?", (tutorial_id,)).fetchone()
    conn.close()
    if not tutorial:
        raise HTTPException(status_code=404, detail="Tutorial not found")
    return dict(tutorial)

@app.get("/api/tutorials/{tutorial_id}/video")
async def stream_video(tutorial_id: int):
    conn = get_db_connection()
    tutorial = conn.execute("SELECT * FROM tutorials WHERE id = ?", (tutorial_id,)).fetchone()
    conn.close()
    if not tutorial or tutorial["status"] != "completed":
        raise HTTPException(status_code=404, detail="Video not ready")
    video_path = tutorial["final_video_path"]
    if not os.path.exists(video_path):
        raise HTTPException(status_code=404, detail="Video file missing")
    return FileResponse(video_path, media_type="video/mp4", filename=f"sparsh_tutorial_{tutorial_id}.mp4")