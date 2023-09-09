y = str()
while (x := input("Введите числовые символы: ")).lower() != "stop":
    if x.isdecimal():
        y += x
        print(y)
    else:
        print("Ошибка! Введено не число!")
else:
    print(y)
