import os
import shutil
import time

path = os.path.join(os.getcwd(), "Proba")
file_life_time = 1
directory_life_time = 2
while True:
    for folder in os.listdir(path):
        full_path = os.path.join(path, folder)
        if os.path.isfile(full_path):
            age = int((time.time() - os.path.getctime(full_path)))
            if age > file_life_time:
                os.remove(full_path)
                print('Deleted file:', folder)
        elif os.path.isdir(full_path):
            dir_age = int((time.time() - os.path.getctime(full_path)))
            if dir_age > directory_life_time:
                shutil.rmtree(full_path)
                print('Deleted directory:', folder)
