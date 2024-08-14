import sys
import time
from watchdog.observers import Observer
from watchdog.events import LoggingEventHandler, PatternMatchingEventHandler
import logging
import getpass
import os
import shutil

def on_modified(event):
    backup_path = 'C:/Users/Usuario/Documents/bkp'
    if(os.path.exists(backup_path)):
        print('pass')
    else:
        print('Not existis')

    try:
        for file_name in os.listdir(path):
            source = path + file_name
            destination = backup_path + file_name

            if os.path.isfile(source):
                shutil.copy(source, destination)
                print(f"Copied: {file_name}")
            else:
                print('Is not file')
    except Exception as e:
        print(e)

class Handler(PatternMatchingEventHandler):
    def __init__(self):
        PatternMatchingEventHandler.__init__(self, patterns=["*.csv"], ignore_directories=True, case_sensitive=True)

    def on_created(self, event):
        print('A new created was made', event.src_path)

    def on_modified(self, event):
        print('A new created was made', event.src_path)

    def on_deleted(self, event):
        print('A deletion was made', event.src_path)
if __name__ == '__main__':
    # user = getpass.getuser()
    # logging.basicConfig(filename='dev.log',filemode='a',level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s' + f' | userid:{user}', datefmt='%m/%d/%Y %I:%M:%S %p')

    path = sys.argv[1] if len(sys.argv) > 1 else '.'
    print(path)

    event_handler = Handler()
    # event_handler.on_modified = on_modified
    observer = Observer()
    observer.schedule(event_handler, path, recursive=True)
    observer.start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
        observer.join()