x = input("Введите пятизначное число: ")
if len(x) == 5 and x.isdecimal():
    for i, s in enumerate(x):
        print(f"{i + 1} цифра равна {s}")
else:
    print("Вы ввели некорректное число!")
