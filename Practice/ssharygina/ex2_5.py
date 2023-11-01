import os
import shutil


def copyfile(source, destination):
    try:
        with open(source, "r") as s:
            t = s.read()
    except FileNotFoundError:
        print(f"Файл не найден!")
        return None
    try:
        with open(destination, "x") as d:
            d.write(t)
            print("Копирование успешно завершено!")
    except FileExistsError:
        print(f"Файл уже существует!")


def copydir(source, destination):
    if not os.path.exists(source):
        print(f"{source} не найдена!")
        return
    if not os.path.isdir(source):
        print(f"{source} не является директорией!")
        return
    if os.path.exists(destination):
        print(f"Директория {destination} уже существует!")
        return
    try:
        shutil.copytree(source, destination)
        print(f"Директория {source} успешно скопирована в директорию {destination}!")
    except (FileNotFoundError, FileExistsError) as e:
        print(e)


source1 = "5"
destination1 = "6"
copydir(source1, destination1)
