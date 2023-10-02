import random


start = int(input("Введите начальное значение диапазона чисел: "))
stop = int(input("Введите конечное значение диапазона чисел: "))
ch = random.randint(start, stop)
num = input("Угадайте число, которое загадал компьютер: ")
while num.isdecimal():
    n = int(num)
    if start <= n <= stop:
        if n == ch:
            print(f"Вы угадали! Компьютер загадал число: {ch}")
            break
        elif n < ch:
            print("Загаданное число больше!")
        else:
            print("Загаданное число меньше!")
    else:
        print("Число не входит в заданный диапазон!")
    num = input("Попробуйте еще: ")
else:
    print("Введено не число!")
