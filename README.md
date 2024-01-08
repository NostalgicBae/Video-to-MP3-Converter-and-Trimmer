# Video to MP3 Converter and Trimmer

This Python script provides a convenient way to convert video files to MP3 format and trim them according to user-specified start and end times. It utilizes the powerful FFmpeg multimedia framework for the conversion process.

## Prerequisites

Before running the script, ensure you have the following installed on your system:
- [FFmpeg](https://ffmpeg.org/download.html)

## Usage

1. Clone the repository:
   ```bash
   git clone https://github.com/NostalgicBae/Video-to-MP3-Converter-and-Trimmer.git
   cd video-to-mp3-converter
   ```
2. Place your video files in the input directory.
3. Run the script:
   ```bash
   python main.py
   ```
4. Follow the on-screen prompts to specify trim start and end times for each video.
5. The converted and trimmed MP3 files will be saved in the output directory.

## Options

- Input Directory: The script looks for video files in the input directory.
- Output Directory: Converted MP3 files are saved in the output directory.
- Trimming: Users can specify start and end times for trimming each video.

## Example

   ```bash
   🎬 Enter trim start time for 'example_video.mp4' (in seconds, or press Enter to skip): 10
   🎬 Enter trim end time for 'example_video.mp4' (in seconds, or press Enter to skip): 60
   ```

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- FFmpeg for the powerful multimedia framework.

## Author

Thomas Blanc Bolelli