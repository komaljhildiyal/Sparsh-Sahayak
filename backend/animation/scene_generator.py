# backend/animation/scene_generator.py

import os

from animation.scenes.text_image_generator import TextImageGenerator
from video.ffmpeg_merger import FFmpegMerger
from animation.prompts.scene_prompt_generator import ScenePromptGenerator


class SceneGenerator:

    def __init__(self):

        self.image_gen = TextImageGenerator()

        self.ffmpeg = FFmpegMerger()

        self.prompt_generator = ScenePromptGenerator()


    def generate_step_video(
        self,
        step_data: dict,
        tutorial_id: int,
        output_dir: str
    ) -> dict:


        step_num = step_data["step_number"]

        hindi_text = step_data["hindi_text"]

        audio_path = step_data["audio_path"]


        # NEW
        visual_prompt = (
            self.prompt_generator.generate_prompt(
                step_data["english_text"]
            )
        )


        image_filename = (
            f"tutorial_{tutorial_id}_step_{step_num}.png"
        )

        video_filename = (
            f"tutorial_{tutorial_id}_step_{step_num}.mp4"
        )


        image_path = os.path.join(
            output_dir,
            "images",
            image_filename
        )

        video_path = os.path.join(
            output_dir,
            "videos",
            video_filename
        )


        print(
            f"Generating image for Step {step_num}",
            flush=True
        )

        print(
            f"Prompt: {visual_prompt}",
            flush=True
        )


        self.image_gen.generate_step_image(
    hindi_text=hindi_text,
    step_number=step_num,
    output_path=image_path
)


        print(
            f"Generating video for Step {step_num}",
            flush=True
        )


        self.ffmpeg.combine_image_audio(
            image_path=image_path,
            audio_path=audio_path,
            output_path=video_path
        )


        step_data["image_path"] = image_path

        step_data["scene_video_path"] = video_path


        return step_data