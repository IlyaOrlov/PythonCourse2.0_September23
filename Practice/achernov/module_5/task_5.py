def replace_chr(file, act):
    with open(file, encoding="utf-8") as file1:
        if act == "свернуть":
            f = file1.read().replace("    ", "\t")
        elif act == "развернуть":
            f = file1.read().replace("\t", "    ")
        else:
            print("Перевыбери")
            return

    with open(file, "w") as file1:
        file1.write(f)


my_file = input("путь до файла: ")
action = input("развернуть или свернуть: ")
replace_chr(my_file, action)
# как-то заработало вроде
