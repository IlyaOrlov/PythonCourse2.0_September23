num = input("Введите пятизначное число: ")
if len(num) == 5 and num.isdecimal():
    for i, s in enumerate(num):
        print(f"{i + 1} цифра равна {s}")
else:
    print("Вы ввели некорректное значение!")
