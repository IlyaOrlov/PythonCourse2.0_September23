import random


def game():
    pass


weapon = ["камень", "ножницы", "бумага"]
bot_choice = random.choice(weapon)
my_choice = input("Выбери камень, ножницы или бумагу: ")

while my_choice == bot_choice:
    print(f"Оба игрока выбрали {my_choice}, Ничья!")
else:
    if (my_choice == "бумага" and bot_choice == "камень" or
            my_choice == "камень" and bot_choice == "ножницы" or
            my_choice == "ножницы" and bot_choice == "бумага"):
        print("Победа")
    else:
        print("Поражение")
