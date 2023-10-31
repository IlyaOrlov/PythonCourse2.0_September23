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


if __name__ == "__main__":
    with open("source", "w", encoding="utf-8") as fs:
        fs.write("я есть!")

    file1 = "source"
    file2 = "destination"
    file3 = "other_source"

    copyfile(file1, file2)  # ok
    copyfile(file1, file2)  # FileExistsError "destination"
    copyfile(file3, file2)  # FileNotFoundError "source"
