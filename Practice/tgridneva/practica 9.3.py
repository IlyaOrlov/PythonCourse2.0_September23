import os
import shutil
import time


def delete_files_and_folders(folder_path):
    while True:
        objects = os.listdir(folder_path)

        for obj in objects:
            obj_path = os.path.join(folder_path, obj)

            if os.path.isfile(obj_path):
                creation_time = os.path.getctime(obj_path)

                if time.time() - creation_time > 60:
                    os.remove(obj_path)
                    print(f"Удален файл: {obj_path}")

            elif os.path.isdir(obj_path):
                creation_time = os.path.getctime(obj_path)

                if time.time() - creation_time > 120:
                    shutil.rmtree(obj_path)
                    print(f"Удалена папка: {obj_path}")

        time.sleep(10)


folder_path = input("Введите путь до папки: ")
delete_files_and_folders(folder_path)
