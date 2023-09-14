import random


while my_choice := input("Выбери камень, ножницы или бумагу: "):
    weapon = ["камень", "ножницы", "бумага"]
    bot_choice = random.choice(weapon)
    if my_choice == bot_choice:
        print(f"Оба игрока выбрали {my_choice}, Ничья! Попробуйте ещё раз!")
    elif (my_choice == "бумага" and bot_choice == "камень" or
          my_choice == "камень" and bot_choice == "ножницы" or
          my_choice == "ножницы" and bot_choice == "бумага"):
        print("Победа")
    else:
        print("Поражение")
