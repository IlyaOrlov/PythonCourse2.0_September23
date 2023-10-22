import os
import time


def close_time_dir_file(path):
    for i in os.listdir(path):
        if os.path.isfile(path + '\\' + i):
            if round(time.time() - os.path.getctime(path + '\\' + i)) > 60:
                print("Файл ", path + '\\' + i, "удален")
                os.remove(path + '\\' + i)
        else:
            if len(os.listdir(path + '\\' + i)) == 0 and (round(time.time() - os.path.getctime(path + '\\' + i)) > 120):
                print(f"Папка ", path + '\\' + i, "удалена")
                os.rmdir(path + '\\' + i)
    for i in os.listdir(path):
        if os.path.isdir(path + '\\' + i):
            close_time_dir_file(path + '\\' + i)


if __name__ == "__main__":
    dir_name = ''
    while dir_name not in os.listdir():
        dir_name = input("Укажите имя папки для контроля, например test: ")
    if len(os.listdir(dir_name)) == 0:
        print("Папка пуста!")
        print("Её нужно заполнить директориями и файлами, секунд за 30-ть :)")
        print("Иначе они протухнут!")
    else:
        while os.listdir(dir_name):
            close_time_dir_file(dir_name)
