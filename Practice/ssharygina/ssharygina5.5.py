def tab_zam(file1, var):
    with open(file1, 'r', encoding="utf-8") as file:
        if var == "развернуть":
            x = file.read().replace("\t", "    ")
        elif var == "свернуть":
            x = file.read().replace("    ", "\t")
        else:
            print("Некорректный ввод")
            return

    with open(file1, 'w') as file:
        file.write(x)


file = input("Введите путь к файлу: ")
var = input("Выберите развернуть или свернуть символы табуляции: ")
tab_zam(file, var)
