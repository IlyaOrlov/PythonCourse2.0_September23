zapros = input("Введите ваш запрос: ")
schet = 0

while zapros != "хватит":

    if schet == 0:
        print("Ты сам-то понял, что написал?")
        schet += 1
    elif schet == 1:
        print("Аргументируй")
        schet += 1
    elif schet == 2:
        print("И?")
        schet = 0

    zapros = input("Введите ваш запрос: ")
