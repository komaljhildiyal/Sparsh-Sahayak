# backend/video/ffmpeg_merger.py

import ffmpeg
import os
import subprocess

class FFmpegMerger:
    
    @staticmethod
    def combine_image_audio(
        image_path: str,
        audio_path: str,
        output_path: str
    ) -> str:

        os.makedirs(
            os.path.dirname(output_path),
            exist_ok=True
        )

        try:

            image = ffmpeg.input(
                image_path,
                loop=1
            )

            audio = ffmpeg.input(
                audio_path
            )

            # Smooth fade only
            animated = image.filter(
                'fade',
                type='in',
                start_time=0,
                duration=1
            )

            stream = ffmpeg.output(
                animated,
                audio,
                output_path,

                vcodec='libx264',
                acodec='aac',
                pix_fmt='yuv420p',

                shortest=None,
                y=None
            )

            ffmpeg.run(
                stream,
                cmd='ffmpeg',
                quiet=True
            )

            return output_path


        except ffmpeg.Error as e:

            stderr_output = (
                e.stderr.decode()
                if e.stderr
                else "Unknown FFmpeg error"
            )

            print(
                f"FFmpeg Error: {stderr_output}",
                flush=True
            )

            raise
    @staticmethod
    def concatenate_videos(video_paths: list, output_path: str) -> str:
        os.makedirs(os.path.dirname(output_path), exist_ok=True)
        list_file_path = os.path.join(os.path.dirname(output_path), "concat_list.txt")
        with open(list_file_path, 'w', encoding='utf-8') as f:
            for path in video_paths:
                safe_path = path.replace("'", "'\\''")
                f.write(f"file '{safe_path}'\n")
        try:
            cmd = [
                'ffmpeg', '-y', '-f', 'concat', '-safe', '0', 
                '-i', list_file_path, '-c', 'copy', output_path
            ]
            
            # CRITICAL: Suppress output to prevent background task freeze
            subprocess.run(cmd, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
            return output_path
            
        except subprocess.CalledProcessError as e:
            print("FFmpeg Concat Error", flush=True)
            raise