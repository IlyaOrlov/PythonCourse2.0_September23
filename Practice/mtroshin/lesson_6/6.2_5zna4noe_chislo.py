ch = input("Введите 5-значное число: ")

while (len(ch) != 5) or not ch.isdecimal():
    ch = input("Введите именно 5-значное и именно число: ")
else:
    for i in range(0, 5):
        print(f"{i + 1} цифра равна {ch[i]}")
