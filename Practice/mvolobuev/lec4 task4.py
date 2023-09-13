import random


def bukv(buk, stops):
    j = 100
    for k in range(0, j):
        zapros = input("Введите любое слово:   ")
        if zapros != stops:
            print(random.choice(buk))
        else:
            return


buk = ("Ты сам понял, что написал?", "Аргументируй", "И")
stops = ("хватит")
bukv(buk, stops)
print("Спасибо за беседу!")
