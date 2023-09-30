def zamena(file, v):
    with open(file, 'r', encoding="utf-8") as f:
        if v == "развернуть":
            z = f.read().replace("\t", "    ")
        elif v == "свернуть":
            z = f.read().replace("    ", "\t")
        else:
            print("Некорректный ввод")
            return

    with open(file, 'w') as f:
        f.write(z)


file = input("Введите путь к файлу: ")
v = input("Выберите развернуть или свернуть символы табуляции: ")
zamena(file, v)
