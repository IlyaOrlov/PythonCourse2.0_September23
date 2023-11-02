import os


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


def copydir(source1, destination1):
    try:
        if not os.path.exists(destination1):
            for super_dirs, dirs, files in os.walk(source1):
                d2 = os.path.join(destination1, os.path.relpath(super_dirs, source1))
                os.makedirs(d2)
                for file in files:
                    s1 = os.path.join(super_dirs, file)
                    d1 = os.path.join(destination1, os.path.relpath(s1, source1))
                    copyfile(s1, d1)
    except FileNotFoundError:
        print(f"Директория {destination1} не существует!")


copydir("5", "dir2")
