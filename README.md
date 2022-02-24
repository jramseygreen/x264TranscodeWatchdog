# x264TranscodeWatchdog
## Dependencies
You must install [ffmpeg](https://ffmpeg.org/download.html) to use this project

install watchdog with pip: `pip install watchdog`

## Usage
In `main.py` add the path to the ffpmeg binary overwriting the `ffmpeg_path` variable (if ffmpeg is not already an evironment variable).

You can optionally change the directories used. If you do not change them then they will be created in the current working directory of the script.
