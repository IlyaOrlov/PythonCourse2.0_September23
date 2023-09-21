def manage_tab(file_name, mode):
    with open(file_name) as file:
        if mode == "wrap":
            s = file.read().replace("\t", "    ")
        elif mode == "unwrap":
            s = file.read().replace("    ", "\t")
        else:
            print("Введен некорректный режим")
            return

    with open(file_name, 'w') as file:
        file.write(s)

    print("Замена символов в файле прошла успешно!")


f = input("Введите имя файла с расширением: ")
m = input("Введите желаемый режим (режим wrap - сворачивание табуляции, режим unwrap - разворачивание): ")
manage_tab(f, m)

