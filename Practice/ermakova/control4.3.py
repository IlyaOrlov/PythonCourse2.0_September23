x = ""
x2 = ""
while (x := input("Введите число: ")).lower() != "stop":
    if x.isdecimal():
        x2 += x
    else:
        print("Вы ввели не число, повторите ввод!")
else:
    print(f"Конец программы! Ваше итоговое число: {x2} ")
