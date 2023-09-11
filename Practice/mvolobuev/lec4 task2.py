n = str(input("Введите пятизначное число: "))
for k in range(0, len(n)):
    print(k+1, end='')
    print(f"  цифра равна:  {n[k]}")
