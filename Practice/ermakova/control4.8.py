import random


igra = ("камень", "бумага", "ножницы")
comp = random.choice(igra)
while (start := input("Напишите что либо, чтобы начать! Когда захотите"
                      " закончить, напишите "
                      "финиш: ")).lower() != "финиш".lower():
    gamer = input("Введите: камень, ножницы или бумага? ").lower()
    if gamer in igra:
        print(f"Вы выбрали {gamer}, компьютер выбрал  {comp}.")
        if gamer == comp:
            print("Ничья!")
        elif gamer == "камень":
            if comp == "бумага":
                print("Вы проиграли!")
            else:
                print("Вы выиграли!")
        elif gamer == "бумага":
            if comp == "ножницы":
                print("Вы проиграли!")
            else:
                print("Вы выиграли!")
        elif gamer == "ножницы":
            if comp == "камень":
                print("Вы проиграли!")
            else:
                print("Вы выиграли!")
    else:
        print("Вы ввели не камень, ножницы или бумага! Начните заново.")
else:
    print("Конец игры!")
