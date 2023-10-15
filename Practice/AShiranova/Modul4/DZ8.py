import random


igra = ("камень", "ножницы", "бумага")
while (start := input("Вы готовы? Напишите что-нибудь, что бы начать игру! Когда захотите"
                      " закончить, напишите стоп: ")).lower() != "стоп":
    comp = random.choice(igra)
    user = input("Введите камень, ножницы или бумага: ").lower()
    if user in igra:
        print(f"Вы выбрали {user}, компьютер выбрал  {comp}.")
        if user == comp:
            print("Ничья!")
        elif user == "камень":
            if comp == "бумага":
                print("Вы проиграли!")
            else:
                print("Вы выиграли!")
        elif user == "бумага":
            if comp == "ножницы":
                print("Вы проиграли!")
            else:
                print("Вы выиграли!")
        elif user == "ножницы":
            if comp == "камень":
                print("Вы проиграли!")
            else:
                print("Вы выиграли!")
    else:
        print("Вы ввели не камень, ножницы или бумага! Начните заново.")
else:
    print("Конец игры!")

