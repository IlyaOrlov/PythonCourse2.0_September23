while not (x := input("Введите числовые символы: ")).isdecimal():
    if x.lower() == "stop":
        print("Конец!")
        break
    else:
        print("Ошибка! Введено не число!")
else:
    print(x)
