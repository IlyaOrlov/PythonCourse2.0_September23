import random


p = int(input("Введите первое число: "))
b = int(input("Введите второе число: "))
num = random.randint(p, b)
i = input("Отгадайте число: ")
while not i.isdecimal() == num:
    x = int(i)
    if x == num:
        print("Вы угадали!")
    elif x > num:
        print(f"Ошибка! Загаданное число меньше!")
        i = input("Попробуйте ещё раз: ")
    else:
        print(f"Ошибка! Загаданное число больше!")
        i = input("Попробуйте ещё раз: ")
else:
    print("Вы ввели не число!")
