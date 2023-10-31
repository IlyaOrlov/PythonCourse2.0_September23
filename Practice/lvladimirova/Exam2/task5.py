import os


def copy_file(source, destination):
    try:
        with open(source, 'r') as f_src:
            data = f_src.read()
        with open(destination, 'x') as f_dest:
            f_dest.write(data)
    except FileNotFoundError as e:
        print("Ошибка: файл", e.filename, "не найден.")
    except FileExistsError as e:
        print("Ошибка: файл", e.filename, "уже существует.")


def copy_dir(source_dir, destination_dir):
    try:
        if not os.path.exists(destination_dir):
            os.makedirs(destination_dir)
        for filename in os.listdir(source_dir):
            source_file = os.path.join(source_dir, filename)
            destination_file = os.path.join(destination_dir, filename)
            if os.path.isfile(source_file):
                copy_file(source_file, destination_file)
            else:
                copy_dir(source_file, destination_file)
    except FileNotFoundError as e:
        print(f"Ошибка: директория: {e.filename} не найдена.")


s_dir = "/path/to/source_dir"
d_dir = "/path/to/destination_dir"
copy_dir(s_dir, d_dir)
