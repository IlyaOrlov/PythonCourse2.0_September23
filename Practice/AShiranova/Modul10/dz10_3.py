import os
import shutil
import time


def deleting(f):
    if os.path.isdir(f):
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
        print("Вы ввели неккоректный путь!")


if __name__ == "__main__":
    way = input("Введите путь до папки: ")
    while True:
        deleting(way)
