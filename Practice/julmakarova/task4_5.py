import random


ran = input("Введите диапазон в формате 'нижняя граница,верхняя граница' (например: 0,10): ")
bord = ran.split(",")
start = int(bord[0])
stop = int(bord[1])
find_num = random.randint(start, stop)
num = input("Угадайте загаданное целое число в заданном диапазоне: ")
while num.isdecimal():
    n = int(num)
    if start <= n <= stop:
        if n == find_num:
            print(f"Ура!Вы справились,загаданное число {find_num}")
            break
        elif n < find_num:
            print("Загаданное число больше!")
        else:
            print("Загаданное число меньше!")
    else:
        print("Введенное число находится за пределами заданного диапазона!")
    num = input("Попробуйте еще: ")
else:
    print("Введено не число!")
