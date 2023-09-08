num = input("Введите число: ")
if len(num) == 5 and num.isdecimal():
    for i, x in enumerate(num, 1):
        print(f"{i} цифра равна {x}")
else:
    print("Ошибка! Попробуй снова")
