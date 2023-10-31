import time
import random


class MyTime:
    def __enter__(self):
        self._start = time.time()

    def __exit__(self, exc_type, exc_val, exc_tb):
        stop = time.time()
        print(f"Время выполнения вашего кода: {stop-self._start} сек")


with MyTime():
    start1 = int(input("Введите начальное значение диапазона чисел: "))
    stop1 = int(input("Введите конечное значение диапазона чисел: "))
    ch = random.randint(start1, stop1)
    num = input("Угадайте число, которое загадал компьютер: ")
    while num.isdecimal():
        n = int(num)
        if start1 <= n <= stop1:
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
