import os
import subprocess

def convert_and_trim_video_to_mp3(input_file, output_file, start_time=None, end_time=None):
    """
    Convert and trim a video file to MP3 format.

    Parameters:
        input_file (str): Path to the input video file.
        output_file (str): Path to the output MP3 file.
        start_time (int or None): Start time for trimming in seconds (optional).
        end_time (int or None): End time for trimming in seconds (optional).
    """
    ffmpeg_cmd = [
        "ffmpeg",
        "-i", input_file,
        "-vn",
        "-acodec", "libmp3lame",
        "-ab", "192k",
        "-ar", "44100",
        "-y"
    ]

    if start_time is not None:
        ffmpeg_cmd.extend(["-ss", str(start_time)])

    if end_time is not None:
        ffmpeg_cmd.extend(["-to", str(end_time)])

    ffmpeg_cmd.append(output_file)

    try:
        subprocess.run(ffmpeg_cmd, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        print(f"✅ Successfully converted and trimmed '{os.path.basename(input_file)}' to '{os.path.basename(output_file)}'!")
    except subprocess.CalledProcessError as e:
        print(f"❌ Conversion failed for '{os.path.basename(input_file)}'. Error: {e}. Failed command: {' '.join(ffmpeg_cmd)}")

# Get the current directory where the main.py script is located
current_directory = os.path.dirname(os.path.abspath(__file__))

# Input and output folders are in the same directory as main.py
input_directory = os.path.join(current_directory, "input")
output_directory = os.path.join(current_directory, "output")

# Ensure input directory exists
if not os.path.exists(input_directory):
    print(f"❌ Input directory '{input_directory}' not found.")
    exit()

# Ensure output directory exists
os.makedirs(output_directory, exist_ok=True)

# List all video files in the input directory
video_files = [filename for filename in os.listdir(input_directory) if filename.endswith(".mp4")]

if not video_files:
    print("❌ No video files found in the input directory.")
    exit()

# Process each video file
for i, filename in enumerate(video_files):
    input_file = os.path.join(input_directory, filename)
    output_file = os.path.join(output_directory, f"{os.path.splitext(filename)[0]}_trimmed_audio.mp3")

    # Prompt user for trim start and end times
    start_time = input(f"🎬 Enter trim start time for '{filename}' (in seconds, or press Enter to skip): ")
    end_time = input(f"🎬 Enter trim end time for '{filename}' (in seconds, or press Enter to skip): ")

    # Convert and trim the video
    convert_and_trim_video_to_mp3(input_file, output_file, start_time if start_time else None, end_time if end_time else None)
