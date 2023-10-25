import os
import shutil
import time


def deleting(f):
    if os.path.isdir(f):
        while True:
            x = os.listdir(f)
            for n in x:
                path = os.path.join(f, n)
                if time.time() - os.path.getctime(path) > 60:
                    os.remove(path)
                    if time.time() - os.path.getctime(path) > 120:
                        shutil.rmtree(path)
    else:
        print("Некорректный путь!")


way = input("Введите путь до папки: ")
deleting(way)
