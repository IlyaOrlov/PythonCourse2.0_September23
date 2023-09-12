ch = input("Введите 5-значное число: ")

while len(ch) != 5 and ch.isdecimal() == False: # почему-то числа с буквами пропускает всеравно
    ch = input("Введите именно 5-значное и именно число: ")
else:
    for i in range(0, 5):
        print(f"{i + 1} цифра равна {ch[i]}")
