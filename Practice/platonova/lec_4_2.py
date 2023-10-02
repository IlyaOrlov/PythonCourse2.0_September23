number = input("Введите пятизначное число: ")
if len(number) == 5 and number.isdecimal():
    for i, x in enumerate(number, 1):
        print(f"{i} цифра равна {x}")
else:
    print("Вы ввели не пятизначное число")
