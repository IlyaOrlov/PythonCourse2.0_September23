import random


def chisl(buk):
    buk = int(buk)
    zapros = input("Угадайте загадоное число от 1 до 10:   ")
    if zapros.isalpha():return
    if int(zapros) == int(buk):
        print("Угадали.  ")
        return
    else:
        zapros = int(zapros)
        if zapros > 10:
            print("Введено число больше 10")
            chisl(buk)
        else:
            if zapros > buk:
                print("Введеное число больше загадоного")
                chisl(buk)
            else:
                print("Введеное число меньше загадоного")
                chisl(buk)


i = random.randint(1, 10)
chisl(i)
print("Спасибо за игру!")
