p = input("Когда вы захотите остановиться, скажите 'STOP'. Введите число: ")
s = ""
p1 = p.lower()
p2 = "stop"
while p1 != p2:
    if p.isalpha():
        print(f"Вы ввели не число!")
        p = input("Введите число: ")
        s += p
    elif p1 == p2:
        break
    else:
        s += p
        p = input("Введите следующие число: ")
print(f"Ваше число: {s}")
