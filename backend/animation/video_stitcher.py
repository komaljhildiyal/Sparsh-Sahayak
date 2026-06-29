# backend/animation/video_stitcher.py

import os
from video.ffmpeg_merger import FFmpegMerger

class VideoStitcher:
    def __init__(self):
        self.ffmpeg = FFmpegMerger()

    def create_final_video(self, steps_data: list, tutorial_id: int, output_dir: str) -> str:
        video_paths = []
        for step in sorted(steps_data, key=lambda x: x["step_number"]):
            if step.get("scene_video_path") and os.path.exists(step["scene_video_path"]):
                video_paths.append(step["scene_video_path"])
        
        if not video_paths:
            raise ValueError("No step videos found to concatenate!")
        
        final_filename = f"sparsh_tutorial_{tutorial_id}.mp4"
        final_output_path = os.path.join(output_dir, "final", final_filename)
        
        return self.ffmpeg.concatenate_videos(video_paths=video_paths, output_path=final_output_path)