x = input("Введите пятизначное число: ")
i = 0
if x.isdecimal() and len(x) == 5:
    for i in range(len(x)):
        print(f"{i+1} цифра равна {x[i]}")
        i += 1
else:
    print("Ошибка! Вы ввели не пятизначное число!")
