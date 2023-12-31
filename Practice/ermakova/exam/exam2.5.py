import os


def copyfile(source, destination):
    try:
        with open(source, 'r') as file:
            content = file.read()
        with open(destination, 'x') as file1:
            file1.write(content)
            print(f"Файл {source} скопирован в {destination}")
    except FileNotFoundError:
        print(f"Файл {source} не найден")
    except FileExistsError:
        print(f"Файл {destination} уже существует")


def copydir(source_dir, destination_dir):
    try:
        if not os.path.exists(destination_dir):
            for super_dirs, dirs, files in os.walk(source_dir):
                d2 = os.path.join(destination_dir, os.path.relpath(super_dirs, source_dir))
                os.makedirs(d2)
                for file in files:
                    s = os.path.join(super_dirs, file)
                    des = os.path.join(destination_dir, os.path.relpath(s, source_dir))
                    copyfile(s, des)
    except FileNotFoundError:
        print(f"Директория {destination_dir} не существует")


copydir('source_directory', 'destination_directory')
