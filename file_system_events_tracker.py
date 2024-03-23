import sys
import time
import random
import os
import shutil
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

from_dir = "C:/Users/tommy/Downloads"

class FileMovementHandler(FileSystemEventHandler): 

    def on_created(self, event):
        print({event.src_path} + "has been created")
    
    def on_modified(self, event):
        print({event.src_path} + "has been modified")

    def on_deleted(self, event):
        print({event.src_path} + "has been deleted")

    def on_moved(self, event):
        print({event.src_path} + "has been moved")

event_handler = FileMovementHandler()

observer = Observer()

# Schedule the Observer
observer.schedule(event_handler, from_dir, recursive=True)

# Start the Observer
observer.start()

try:
    while True:
        time.sleep(2)
        print("running...")
except KeyboardInterrupt:
    print("stopped!")
    observer.stop()