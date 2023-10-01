ch = input("Введите пятизначное число: ")
if len(ch) == 5 and ch.isdecimal():
    for i, s in enumerate(ch):
        print(f"{i + 1} цифра равна {s}")
else:
    print("Ошибка ввода!")
    