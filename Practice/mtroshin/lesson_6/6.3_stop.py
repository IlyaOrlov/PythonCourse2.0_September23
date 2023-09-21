ch = ""
symbol = ""

while (symbol := input("Введите число: ")).lower() != "stop":
    if not symbol.isdecimal():
        print("Ошибка! Вы ввели не числовой символ")
    else:
        ch += symbol
        print(ch)
