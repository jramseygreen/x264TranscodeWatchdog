import os
import time

from Watcher import Watcher

class Transcoder:
    def __init__(self, ffmpeg_path="ffmpeg", input_dir=None, processing_dir=None, output_dir=None):
        self.ffmpeg_path = ffmpeg_path

        if not input_dir:
            input_dir = os.getcwd() + os.sep + "transcode"
        if not processing_dir:
            processing_dir = os.getcwd() + os.sep + ".in_progress"
        if not output_dir:
            output_dir = os.getcwd() + os.sep + "completed"

        self.input_dir = input_dir
        self.processing_dir = processing_dir
        self.output_dir = output_dir

        self.watcher = Watcher(path=self.input_dir, on_created=self.on_created)

    def start(self):
        try:
            os.mkdir(self.input_dir)
            os.mkdir(self.processing_dir)
            os.mkdir(self.output_dir)

        finally:
            self.watcher.start()

    def stop(self):
        self.watcher.stop()

    def on_created(self, event):
        if not event.is_directory and os.path.exists(event.src_path):
            historicalSize = -1
            while (historicalSize != os.path.getsize(event.src_path)):
                historicalSize = os.path.getsize(event.src_path)
                time.sleep(1)
            time.sleep(1)
            if not os.path.exists(self.output_dir + os.sep + event.src_path.replace(self.input_dir + os.sep, "") + ".mp4"):
                os.makedirs(os.path.dirname(self.processing_dir + os.sep + event.src_path.replace(self.input_dir + os.sep, "") + '.mp4'), exist_ok=True)
                os.system(self.ffmpeg_path + ' -i "' + event.src_path + '" -bsf:v h264_mp4toannexb -sn -map 0:0 -map 0:1 -vcodec libx264 "' + self.processing_dir + os.sep + event.src_path.replace(self.input_dir + os.sep, "") + '.mp4"')
                os.makedirs(os.path.dirname(self.output_dir + os.sep + event.src_path.replace(self.input_dir + os.sep, "") + '.mp4'), exist_ok=True)
                os.replace(self.processing_dir + os.sep + event.src_path.replace(self.input_dir + os.sep, "") + '.mp4', self.output_dir + os.sep + event.src_path.replace(self.input_dir + os.sep, "") + '.mp4')
            os.remove(event.src_path)
