import os
import shutil


def copy_file(source, destination):
    try:
        with open(source, 'r') as f_src:
            data = f_src.read()
        with open(destination, 'x') as f_dest:
            f_dest.write(data)
    except (FileNotFoundError, FileExistsError) as e:
        print(e)


def copydir(source, destination):
    if not os.path.exists(source):
        print(f"Данный файл {source} не существует")
        return
    if not os.path.isdir(source):
        print(f"Файл {source} не является директорией")
        return
    if os.path.exists(destination):
        print(f"Папка {destination}уже существует")
        return
    try:
        shutil.copytree(source, destination)
        print(f"Папка {source} успешно скопирована в {destination}")
    except (FileNotFoundError, FileExistsError) as e:
        print(e)


source_dir = "source_directory"
destination_dir = "destination_directory"
copydir(source_dir, destination_dir)
