def zamena(file, v):
    with open(f"{file}", 'r', encoding="utf-8") as f:
        if v == "развернуть":
            f.read().replace("\t", "    ")
        elif v == "свернуть":
            f.read().replace("    ", "\t")
        else:
            print("Некорректный ввод")
    return file


file = input("Введите путь к файлу: ")
v = input("Выберите развернуть или свернуть символы табуляции: ")
d = zamena(file, v)
