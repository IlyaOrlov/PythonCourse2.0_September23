import os
import time
from pathlib import Path


def close_time_dir_file(path):
    for i in os.listdir(path):
        cur_path = Path(path, i)
        if cur_path.is_file():
            if round(time.time() - cur_path.stat().st_ctime) > 60:
                print("Файл ", cur_path, "удален")
                cur_path.unlink()
        if cur_path.is_dir():
            if len(os.listdir(cur_path)) == 0 and (round(time.time() - cur_path.stat().st_ctime) > 120):
                print(f"Папка ", cur_path, "удалена")
                cur_path.rmdir()
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
