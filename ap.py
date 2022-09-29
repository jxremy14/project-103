from msilib.schema import File
import sys
import time
import random
import os
import shutil
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import logging

from_dir="C:\Users\class\OneDrive\Desktop\project 103\testfolder"
class FileEventHandler(FileSystemEventHandler):

    def on_created(self,event):
        print(f"hey,{event.src_path}has been created")

    def on_deleted(self,event):
        print(f"hey,someone has deleted{event.src_path}!")   

    def on_modified(self,event):
        print(f"hey,{event.src_path}has been modifed")
    def on_moved(self,event):
        print(f"someone moved{event.src_path}to{event.dest_path}")

event_handle=FileEventHandler()
observer=Observer()

observer.schedule(event_handler,from_dir,recursive=True)

observer.start()

try:
    while True:
        time.sleep(2)
        print("running")

except KeyboardInterrupt:
    print("stopped")
    observer.stop()
        