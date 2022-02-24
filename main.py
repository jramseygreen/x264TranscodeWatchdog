from Transcoder import Transcoder

# Modify below
ffmpeg_path = "ffmpeg"

input_dir = None
processing_dir = None
output_dir = None

transcoder = Transcoder(ffmpeg_path, input_dir, processing_dir, output_dir)
transcoder.start()
