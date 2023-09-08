while not ((x := input("Введите пятизначное число ")).isdecimal() and len(x) == 5):
    pass

i = 0
while i < len(x):
    if x[i].isdecimal():
        print(f"{i+1} цифра равна {x[i]}\n")
    i += 1
