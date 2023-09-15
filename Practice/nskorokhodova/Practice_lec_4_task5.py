import random


if __name__ == "__main__":
    x = int(input("Введите число начала диапазона: "))
    y = int(input("Введите число конца диапазона: "))
    number = random.randint(x, y)
    while (s := input("Угадайте число: ")).isdecimal():
        s = int(s)
        if x <= s <= y:
            if s == number:
                print("Верно, мои поздравления!")
                break
            elif s < number:
                print("Загаданное число больше! Попытайтесь еще!")
            else:
                print("Загаданное число меньше! Попытайтесь еще!")
        else:
            print("Число не входит в диапазон!")
    else:
        print("Это не число, попытайтесь еще!")
