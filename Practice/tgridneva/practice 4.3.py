number = ""
number2 = ""
while (number := input("Введите число: ")).lower() != 'stop':
    if number.isdecimal():
        number2 += number
    else:
        print("Введено не число, повторите ввод: ")
else:
    print(f"Конец программы! Ваше итоговое число: {number2} ")
