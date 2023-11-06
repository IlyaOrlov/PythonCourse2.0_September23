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


source1 = "1.txt"
destination1 = "2.txt"

copyfile(source1, destination1)
