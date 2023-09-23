def fun_zamena(file, x):
    with open(file, encoding="utf-8") as file1:
        if x == "свернуть":
            s = file1.read().replace("    ", "\t")
        elif x == "развернуть":
            s = file1.read().replace("\t", "    ")
        else:
            print("Вы ввели неправильный режим работы")
            return

    with open(file, 'w') as file1:
        file1.write(s)


doc = input("Введите файл с расширением: ")
r = input("Выберите действие с файлом (свернуть или развернуть табуляцию): ")
