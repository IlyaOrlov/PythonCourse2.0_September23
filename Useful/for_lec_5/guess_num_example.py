import random


num = random.randint(1, 10)
i = input("Отгадайте число: ")
if i.isdecimal():
    x = int(i)
    if x == num:
        print("Вы угадали!")
    elif x > num:
        print("Ошибка! Загаданное число меньше!")
    else:
        print("Ошибка! Загаданное число больше!")
else:
    print("Вы ошиблись!")
