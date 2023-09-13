import random

answer=""

d1 = input("Введите начало диапазона ")
d2 = input("Введите конец диапазона ")

chislo = random.randrange(int(d1),int(d2))
answer = input("Угадай загаданное число: ")

while int(answer) != chislo:
    if answer.isdecimal() == False:
         print("Ошибка! Введите именно число!")
    else:
        if int(answer) < chislo:
            print("Загаданное число больше")
        else:
            print("Загаданное число меньше")
    answer = input("Попробуй угадать снова: ")

print("Вы угадали!")
