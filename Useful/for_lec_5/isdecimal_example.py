x = input("Введите число: ")
if x.isdecimal():
    x = int(x)
    y = input("Введите число: ")
    if y.isdecimal():
        y = int(y)
        print(f"Сумма: {x + y}")
    else:
        print("Введено не число")
else:
    print("Введено не число")