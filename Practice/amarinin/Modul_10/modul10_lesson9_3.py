import os
import time
import shutil
from pathlib import Path


def close_time_dir_file(path):
    for i in os.listdir(path):
        # cur_path = os.path.join(path, i)
        cur_path = Path(path, i)
        if os.path.isfile(cur_path):
            if round(time.time() - os.path.getctime(cur_path)) > 60:
                print("Файл ", cur_path, "удален")
                os.remove(cur_path)
        if os.path.isdir(cur_path):
            if len(os.listdir(cur_path)) == 0 and (round(time.time() - os.path.getctime(cur_path)) > 120):
                print(f"Папка ", cur_path, "удалена")
                shutil.rmtree(cur_path)
            else:
                close_time_dir_file(cur_path)


if __name__ == "__main__":
    dir_name = ''
    while dir_name not in os.listdir():
        dir_name = input("Укажите имя папки для контроля, например test: ")
    if len(os.listdir(dir_name)) == 0:
        print("Папка пуста!")
        print("Её нужно заполнить директориями и файлами, секунд за 30-ть :)")
        print("Иначе они протухнут!")
    else:
        print("Погнали!")
        while os.listdir(dir_name):
            close_time_dir_file(dir_name)
