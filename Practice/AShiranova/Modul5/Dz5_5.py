def manage_tab(file_name, mode):
    with open(file_name) as file:
        if mode == "свернуть":
            s = file.read().replace("\t", "    ")
        elif mode == "развернуть":
            s = file.read().replace("    ", "\t")
        else:
            print("Введен некорректный режим")
            return

    with open(file_name, 'w') as file:
        file.write(s)

    print("Замена прошла успешно")


f = input("Введите имя объекта(свойства файла, вкладка безопасность): ")
m = input("Введите желаемый режим (свернуть/развернуть): ")
manage_tab(f, m)
