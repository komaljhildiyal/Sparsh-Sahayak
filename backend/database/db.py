import sqlite3
import os

DB_PATH = os.path.join(os.path.dirname(__file__), "sparsh_tutorials.db")

def get_db_connection():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS tutorials (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            topic TEXT NOT NULL,
            status TEXT DEFAULT 'pending',
            final_video_path TEXT,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS steps (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            tutorial_id INTEGER NOT NULL,
            step_number INTEGER NOT NULL,
            english_text TEXT,
            hindi_text TEXT,
            audio_path TEXT,
            image_path TEXT,
            scene_video_path TEXT,
            status TEXT DEFAULT 'pending',
            FOREIGN KEY (tutorial_id) REFERENCES tutorials (id)
        )
    ''')

    conn.commit()
    conn.close()
    print("Database initialized successfully!", flush=True)