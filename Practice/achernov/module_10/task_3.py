import os
import shutil
import time


def deleter(path):
    if os.path.exists(path):
        while True:
            for r, dr, files in os.walk(path):
                for file in files:
                    f_path = os.path.join(r, file)
                    if time.time() - os.path.getctime(f_path) > 60:
                        os.remove(f_path)
                for d_name in dr:
                    d_path = os.path.join(r, d_name)
                    if time.time() - os.path.getctime(d_path) > 120:
                        shutil.rmtree(d_path)
    else:
        print("Неверный путь, либо не существует")


my_path = input("Укажите путь: ")
deleter(my_path)
