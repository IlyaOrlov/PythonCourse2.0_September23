import random


start = int(input("Начало диапазона: "))
stop = int(input("Конец диапазона: "))
fun = random.randrange(start, stop, 1)
s_fun = str(fun)
while (x := input("Угадайте число: ")) != s_fun:
    if x.isdecimal():
        x = int(x)
        if x < fun:
            print("Загаданное число больше.")
        else:
            print("Загаданное число меньше.")
    else:
        print("Вы ввели не число! Попробуйте ещё раз.")
else:
    print("Угадано!")