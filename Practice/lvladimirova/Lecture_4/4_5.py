import random
if __name__ == "__main__":
    start = int(input("Введите начало диапазона: "))
    finish = int(input("Введите конец диапазона: "))
    number = random.randint(start, finish)
    print(number)
    while (x := input("Угадайте число: ")).isdecimal():
        x = int(x)
        if start <= x <= finish:
            if x == number:
                print("Поздравляю! Вы угадали!")
                break
            elif x < number:
                print("Загаданное число чуть больше! Ещё попытка!")
            else:
                print("Загаданное число чуть меньше! Ещё попытка!")
        else:
            print("Число не входит в диапазон!")
    else:
        print("Вы ввели не число!")
