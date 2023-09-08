num = input("Введите число: ")
if len(num) == 5 and num.isdecimal():
    for i, x in enumerate(num):
        print(f"{i + 1} цифра равна {x}")
else:
    print("Ошибка! Попробуй снова")
