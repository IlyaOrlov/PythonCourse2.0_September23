import os
import time
import shutil

folder = "3_folder"

while True:
    for (path, dirs, files) in os.walk(folder):
        for name in files:
            is_file = os.path.join(path, name)
            is_time = time.time()-os.path.getctime(is_file)
            print(f"Файл {is_file} существует: {is_time}")
            if is_time > 60:
                os.remove(is_file)
                print(f"Файл {is_file} удален")
        for name_2 in dirs:
            is_dir = os.path.join(path, name_2)
            is_time2 = time.time()-os.path.getctime(is_dir)
            print(f"Папка {is_dir} существует: {is_time2}")
            if is_time2 > 120:
                print(f"Папка {is_dir} удалена")
                shutil.rmtree(is_dir)
    time.sleep(5)

