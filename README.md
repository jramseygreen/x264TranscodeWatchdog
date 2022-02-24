# x264TranscodeWatchdog
## Dependencies
You must install [ffmpeg](https://ffmpeg.org/download.html) to use this project

install watchdog with pip: `pip install watchdog`

## Setup
In `main.py` add the path to the ffpmeg binary overwriting the `ffmpeg_path` variable (if ffmpeg is not already an evironment variable).

You can optionally change the directories used. If you do not change them then they will be created in the current working directory of the script.

## Usage

Drop any video files into the input directory to be transcoded to the x264 codec. 
The transcoded files will appear in the output directory once completed and will delete the original.
