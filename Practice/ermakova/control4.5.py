import random


start = int(input("Введите начало диапазона: "))
finish = int(input("Введите конец диапазона: "))
num = random.randint(start, finish)
while (i := input("Угадайте целое число из этого диапазона: ")).isdecimal():
    numi = int(i)
    if start <= numi <= finish:
        if numi == num:
            print(f"Ура! Вы угадали, Ваше число: {num}")
            break
        if numi < num:
            print(f"Ошибка! Загаданное число больше!")
        else:
            print(f"Ошибка! Загаданное число меньше!")
    else:
        print("Ваше число не из этого дипазона!!!")
else:
    print(f"Вы ввели не  число!")
