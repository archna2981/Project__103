#importing libraries
import sys
import time
import os
import random
import shutil

from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

from_dir = "C:\Users\Pragya\Downloads"

#Event Hanlder Class
class FileEventHandler(FileSystemEventHandler):
    def on_created(self, event):
        print(f"Hey, {event.src_path} has been created!")

    def on_modified(self, event):
        print(f"Hey, {event.src_path} has been modified!")

    def on_moved(self, event):
        print(f"Hey, {event.src_path} has been moved!")

    def on_deleted(self, event):
        print(f"Oops! Someone deleted {event.src_path}!")

#Initialize Event Handler Class
event_handler = FileEventHandler()

#Initialize Observer
observer = Observer()

#Schedule the Observer
observer.schedule(event_handler, from_dir, recursive=True)

#Start the Observer
observer.start()

try:
    while True:
        time.sleep(2)
        print("Running...")
except KeyboardInterrupt:
    print("Stopped!")
    observer.stop()







