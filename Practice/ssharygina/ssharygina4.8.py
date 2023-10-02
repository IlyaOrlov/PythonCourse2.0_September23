import random


def igra(user):
    var = ["камень", "ножницы", "бумага"]
    comp = random.choice(var)
    print(f"Пользователь выбрал: {user}, а Компьютер выбрал: {comp}")
    if user == comp:
        print("Ничья!")
    elif (user == "камень" and comp == "ножницы" or user == "ножницы" and comp == "бумага" or
          user == "бумага" and comp == "камень"):
        print("Вы победили!")
    else:
        print("Вы проиграли!")


vopr = input("Сыграем в игру Камень, ножницы, бумага? ").lower()
while vopr == "да":
    vopr = input("Камень, ножницы, бумага, раз, два, три!\nВведите ваш вариант: ").lower()
    if vopr == "камень" or vopr == "ножницы" or vopr == "бумага":
        igra(vopr)
    else:
        print("Вы ввели некорректное значение!")
    vopr = input("Повторим? ")
print("Конец")
