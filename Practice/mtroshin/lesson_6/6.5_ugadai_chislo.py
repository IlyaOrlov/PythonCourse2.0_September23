import random

answer=""

d1 = input("Введите начало диапазона ")
d2 = input("Введите конец диапазона ")

chislo = random.randrange(int(d1),int(d2))
answer = input("Угадай загаданное число: ")



while (answer := input("Попробуй угадать снова: ")) != str(chislo):
    if not answer.isdecimal():
        print("Ошибка! Введите именно число!")
    else:
        if int(answer) < chislo:
            print("Загаданное число больше")
        else:
            print("Загаданное число меньше")

print("Вы угадали!")
