import sys
import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

class Watcher:
    def __init__(self, path="", on_created=None, on_deleted=None, on_modified=None, on_moved=None):
        self.event_handler = FileSystemEventHandler()
        self.observer = Observer()

        self.running = False
        self.path = path

        if on_created:
            self.on_created(on_created)
        if on_deleted:
            self.on_deleted(on_deleted)
        if on_modified:
            self.on_modified(on_modified)
        if on_moved:
            self.on_moved(on_moved)

    # events - passes event object with event.event_type, event.src_path, event.is_directory
    def on_created(self, method):
        self.event_handler.on_created = method

    def on_deleted(self, method):
        self.event_handler.on_deleted = method

    def on_modified(self, method):
        self.event_handler.on_modified = method

    def on_moved(self, method):
        self.event_handler.on_moved = method

    def set_path(self, path):
        self.path = path

    def start(self):
        self.running = True
        self.observer.schedule(self.event_handler, self.path, recursive=True)
        self.observer.start()
        try:
            while self.running:
                time.sleep(1)
        finally:
            self.observer.stop()
            self.observer.join()

    def stop(self):
        self.running = False
