import random


def game(player):
    variants = ["Камень", "Ножницы", "Бумага"]
    bot = random.choice(variants)
    print(f"{player} VS {bot}")
    if player == bot:
        print("Ничья!")
    elif (player == "Камень" and bot == "Ножницы" or player == "Ножницы" and bot == "Бумага" or
          player == "Бумага" and bot == "Камень"):
        print("Ура! Вы победили! :)")
    else:
        print("К сожалению, Вы проиграли! :(")


ans = input("Сыграем в игру Камень, Ножницы,Бумага? Да/Нет -> ")
while ans == "Да":
    ans = input("Поехали! Камень, Ножницы, Бумага, раз, два, три: -> ")
    if ans == "Камень" or ans == "Ножницы" or ans == "Бумага":
        game(ans)
    else:
        print("Вы ввели некорректное значение!")
    ans = input("Сыграем еще разок? Да/Нет -> ")
print("До встречи!:)")
