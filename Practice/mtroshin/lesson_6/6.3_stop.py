symbol = input("Введите число: ")
ch = ""
while symbol.lower() != "stop":
    if symbol.isdecimal() != True:
        print("Ошибка! Вы ввели не числовой символ")
    else:
        ch = ch + symbol
        print(ch)
    symbol = input("Введите число: ")
