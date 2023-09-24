import random


lst = ["камень", "ножницы", "бумага"]
choice = random.choice(lst)
print(f"Приветствую тебя, я хочу сыграть с тобой в игру!")
p = input("Введите камень, ножницы или бумагу: ").lower()
if p == choice:
    print("Ничья!")
elif p == "камень" and choice == "ножницы":
    print(f"Ваш выбор: {p}, выбор компьютера: {choice}. Вы выйграли")
elif p == "ножницы" and choice == "камень":
    print(f"Ваш выбор: {p}, выбор компьютера: {choice}. Вы проиграли")
elif p == "ножницы" and choice == "бумага":
    print(f"Ваш выбор: {p}, выбор компьютера: {choice}. Вы выйграли")
elif p == "бумага" and choice == "ножницы":
    print(f"Ваш выбор: {p}, выбор компьютера: {choice}. Вы проиграли")
elif p == "бумага" and choice == "камень":
    print(f"Ваш выбор: {p}, выбор компьютера: {choice}. Вы выйграли")
elif p == "камень" and choice == "бумага":
    print(f"Ваш выбор: {p}, выбор компьютера: {choice}. Вы выйграли")
else:
    print("Вы ввели что-то не то")
