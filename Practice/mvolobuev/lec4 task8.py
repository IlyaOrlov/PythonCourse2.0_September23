import random


def bukv(buky):
    for k in range(0, 100):
        zapros = input("Выберите одно из трех слов и введите его (Камень, Ножницы, Бумага), для выхода введите Хватит:   ")
        zapros = zapros.strip()
        zapros = zapros.lower()

        if zapros == buky[3]: return

        if zapros not in buky:
            print("Слово введено с ошибкой, введите слово заново")
        else:
            i = random.randint(0, 2)
            if zapros == buky[i]:
                print(f"Мы выбрали тоже: {zapros}")
            else:
                if i == 0:
                    if zapros == buky[1]: print (f"{buky[i]} Вы проиграли")
                    if zapros == buky[2]: print(f"{buky[i]} Вы выиграли")
                if i == 1:
                    if zapros == buky[0]: print (f"{buky[i]} Вы выиграли")
                    if zapros == buky[2]: print(f"{buk[i]} Вы проиграли")
                if i == 2:
                    if zapros == buky[0]:print(f"{buky[i]} Вы проиграли")
                    if zapros == buky[1]: print(f"{buky[i]} Вы выиграли")



buk = ["камень", "ножницы", "бумага", "хватит"]
bukv(buk)
print("Спасибо за игру!")