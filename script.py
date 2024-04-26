import os
import shutil
import sys
import time
import random
from watchdog.observers import Observer
from watchdog.events import FileSystemEvent, FileSystemEventHandler

from_dir = '/Users/grishka/Downloads';
to_dir = '/Users/grishka/Documents'
list_of_files = os.listdir(from_dir)

class FileEventHandler(FileSystemEventHandler):
    def on_created(self, event):
        print(f"Hey, {event.src_path} has been created")

    def on_deleted(self, event):
        print(f"Oops! someone deleted {event.src_path}")

    def on_moved(self, event):
        print(f"Hey! {event.src_path} has been moved")

    def on_modified(self, event):
        print(f"Hey! {event.src_path} has been modified")

# Initialize event handler class
event_handler = FileEventHandler();

# Intitialsize observer
observer = Observer();

# Schedule the observer
observer.schedule(event_handler, from_dir, recursive=True)

# Start the observer
observer.start()

while True:
    time.sleep(2);
    print('running')









# for file in list_of_files:
#     root, extension = os.path.splitext(file)

#     if extension == '':
#         continue

#     if extension in ['.txt', '.doc', 'docx', 'pdf']:
#         path1 = from_dir + '/' + file
#         path2 = to_dir + '/' + 'Document_Files'
#         path3 = path2 + '/' + file

#         print(to_dir, path2)

        
#         print('Moving')
#         shutil.move(path1, path3)
            
        