p = input("Введите пятизначное число: ")
p1 = p[0]
k = 0
while k < len(p):
    print(f"{k + 1} цифра равна ", p[k])
    k += 1
