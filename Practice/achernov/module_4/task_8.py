import random


weapon = ["камень", "ножницы", "бумага"]
bot_choice = random.choice(weapon)


while (my_choice := input("Выбери камень, ножницы или бумагу: ")).lower():
    if my_choice == bot_choice:
        print(f"Оба игрока выбрали {my_choice}, Ничья!")
    elif (my_choice == "бумага" and bot_choice == "камень" or
          my_choice == "камень" and bot_choice == "ножницы" or
          my_choice == "ножницы" and bot_choice == "бумага"):
        print("Победа")
    else:
        print("Поражение")
    break
