import os
from pathlib import Path


def copyfile(f1, f2):
    try:
        with open(f1, "r", encoding="utf-8") as f:
            data = f.read()
        with open(f2, "x", encoding="utf-8") as f:
            f.write(data)
    except FileNotFoundError:
        print(f"такого файла {f1} нет :(")
    except FileExistsError:
        print(f"такой файл {f2} уже есть :)")
    else:
        print(f"хо-хо!! {f1}  скопирован в {f2}")


def copydir(d1, d2):
    if not os.path.exists(d2):
        os.mkdir(d2)
    for i in os.listdir(d1):
        cur_path1 = Path(d1, i)
        cur_path2 = Path(d2, i)
        if cur_path1.is_file():
            copyfile(Path(d1, "source"), Path(d2, "destination"))
        else:
            copydir(cur_path1, cur_path2)


if __name__ == "__main__":
    dir1 = "dir_source"
    dir2 = "dir_destination"
    file1 = "source"
    if not os.path.exists(dir1):
        os.mkdir(dir1)
    path_file1 = Path(dir1, file1)
    with open(path_file1, "w", encoding="utf-8") as fs:
        fs.write("я сново здесь")
    copydir(dir1, dir2)
