import random


def chisl(buk, a, b):
    a = int(a)
    b = int(b)
    buk = int(buk)
    zapros = input("Угадайте загадоное число в заданном дипазоне:   ")
    if zapros.isdigit():
        print(f"{zapros}")
        if int(zapros) == int(buk):
            print("Угадали.  ")
            return zapros
        else:
            zapros = int(zapros)
            if zapros > b:
                print("Введено число больше верхнего диапазона")
                chisl(buk, a, b)
            else:
                if zapros < a:
                    print("Введено число меньше нижнего  диапазона")
                    chisl(buk, a, b)
                else:
                    if zapros > buk:
                        print("Введеное число больше загадоного")
                        chisl(buk, a, b)
                    else:
                        print("Введеное число меньше загадоного")
                        chisl(buk, a, b)
    else:
        print("Введена точка")
        return zapros


a = int(input("Введите цифру, начало диапазона :   "))
b = int(input("Введите цифру, конец диапазона :   "))
i = random.randint(a, b)
chisl(i, a, b)
print("Спасибо за игру!")
