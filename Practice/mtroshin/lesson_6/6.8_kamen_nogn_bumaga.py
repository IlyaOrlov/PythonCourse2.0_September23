import random

rukaUser = input("Введите 'камень' или 'ножницы' или 'бумага': ")
variant = ['камень', 'ножницы', 'бумага']
rukaPC = random.choice(variant)
print(f"ПК показывает: {rukaPC}")
if rukaUser == rukaPC:
    print("Ничья")
elif rukaUser == "камень":
    if rukaPC == "ножницы":
        print("Вы победили!")
    else:
        print("Вы проиграли!")
elif rukaUser == "ножницы":
    if rukaPC == "камень":
        print("Вы проиграли!")
    else:
        print("Вы победили!")
elif rukaUser == "бумага":
    if rukaPC == "камень":
        print("Вы победили!")
    else:
        print("Вы проиграли!")


