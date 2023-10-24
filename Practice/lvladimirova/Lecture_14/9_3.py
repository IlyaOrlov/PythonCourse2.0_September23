import os
import shutil
import sys
import time


def delete_files_and_folders(path):
    try:
        for root, dirs, files in os.walk(path):
            for name in files:
                if os.path.getctime(os.path.join(root, name)) < time.time() - 60:
                    os.remove(os.path.join(root, name))

            for name in dirs:
                full_path = os.path.join(root, name)

                if (os.path.isdir(full_path)) and (os.path.getmtime(full_path) < time.time() - 120):
                    shutil.rmtree(full_path)
    except Exception as e:
        print("Ошибка при удалении файлов и папок: ", e)


sys.path = os.path.join(os.getcwd(), "Proba")
while True:
    delete_files_and_folders(sys.path)
