
schet = 0

while (zapros := input("Введите ваш запрос: ")) != "хватит":

    if schet == 0:
        print("Ты сам-то понял, что написал?")
        schet += 1
    elif schet == 1:
        print("Аргументируй")
        schet += 1
    elif schet == 2:
        print("И?")
        schet = 0
