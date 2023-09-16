s = ""
while (p := input("Введите число, когда захотите остановиться введите 'STOP': ")).lower() != "stop":
    if p.isdecimal():
        s += p
    else:
        print(f"Вы ввели не число!")
    print(s)
print(f"Ваше число: {s}")

