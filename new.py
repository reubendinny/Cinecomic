import os
import subprocess

def extract_frames(video_path, output_dir):
    os.makedirs(output_dir, exist_ok=True)

    # Use ffmpeg to extract 2 frames per second
    subprocess.call([
        "ffmpeg",
        "-i", video_path,
        "-vf", "fps=2",
        os.path.join(output_dir, "frame_%04d.png")
    ])

# Example usage
video_path = "./video/IronMan.mp4"
output_directory = "./frames"

extract_frames(video_path, output_directory)











