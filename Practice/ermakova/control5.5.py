def fun_zamena(control_file, kod):
    with open(control_file, "r+", encoding="utf-8") as file1:
        if kod == "пробелы":
            tst = file1.read().replace("\t", "    ")
            print(tst)
        elif kod == "таб":
            tst = file1.read().replace("    ", "\t")
            print(tst)
        else:
            print("Вы ввели неверную опцию")
            return
    with open(control_file, "w", encoding="utf-8") as file1:
        file1.write(tst)


with open("control.txt", "w", encoding="utf-8") as file:
    file.write('winter,    spring,    summer,\tautumn')
with open("control.txt", "r", encoding="utf-8") as file:
    res = file.read()
    print(res)

x = input("Введите ваше опцию(таб или пробелы): ")
fun_zamena("control.txt", x)
