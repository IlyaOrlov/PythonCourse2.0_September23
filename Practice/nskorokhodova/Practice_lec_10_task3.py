import os
import time
import shutil


def delete_files_and_folders(path, expiration_time):
    current_time = time.time()

    try:
        for root, dirs, files in os.walk(path):
            for file_name in files:
                file_path = os.path.join(root, file_name)

                creation_time = os.path.getctime(file_path)

                if (current_time - creation_time) > expiration_time:
                    os.remove(file_path)

            for dir_name in dirs:
                dir_path = os.path.join(root, dir_name)

                creation_time = os.path.getctime(dir_path)

                if (current_time - creation_time) > expiration_time:
                    shutil.rmtree(dir_path)

        print("Файлы и папки, у которых истек срок:", path)

    except Exception as e:
        print("Ошибка при удалении файлов и папок:", str(e))
