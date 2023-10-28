import os
import shutil
import time


def deleting(f):
    if os.path.isdir(f):
        while True:
            x = os.listdir(f)
            for n in x:
                pat = os.path.join(f, n)
                if os.path.isfile(pat):
                    if time.time() - os.path.getctime(pat) > 60:
                        os.remove(pat)
                elif os.path.isdir(pat):
                    deleting(pat)
                    if time.time() - os.path.getctime(pat) > 120:
                        shutil.rmtree(pat)
    else:
        print("Некорректный путь!")


way = input("Введите путь до папки: ")
deleting(way)
