import os
import shutil


def copy_file(source, destination):
    try:
        if os.path.isfile(source):
            with open(source, 'r') as f_src:
                data = f_src.read()
            with open(destination, 'x') as f_dest:
                f_dest.write(data)
        elif os.path.isdir(source):
            shutil.copytree(source, destination)
        else:
            raise ValueError("Неверный путь")
    except (FileNotFoundError, FileExistsError, ValueError) as e:
        print(e)


source_file = "file1.txt"
destination_file_valid = "file2.txt"
copy_file(source_file, destination_file_valid)

source_dir = "dir1"
destination_dir = "dir2"
copy_file(source_dir, destination_dir)
