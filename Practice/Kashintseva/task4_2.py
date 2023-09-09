x = input("Введите пятизначное число: ")
if x.isdecimal() and len(x) == 5:
    for i in range(len(x)):
        print(f"{i+1} цифра равна {x[i]}")
else:
    print("Ошибка! Вы ввели не пятизначное число!")
