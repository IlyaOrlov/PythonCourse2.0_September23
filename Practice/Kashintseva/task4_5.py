import random


start = int(input("Введите начальное значение диапазона: "))
end = int(input("Введите конечное значение диапазона: "))
num = random.randint(start, end)
while (x := input("Угадайте целое число: ")) != str(num):
    if x.isdecimal():
        x = int(x)
        if x < num:
            print("Не угадали. Загаданное число больше.")
        else:
            print("Не угадали. Загаданное число меньше.")
    else:
        print("Вы ввели не число! Попробуйте ещё раз.")
else:
    print("Вы великолепны! Число угадано!")
