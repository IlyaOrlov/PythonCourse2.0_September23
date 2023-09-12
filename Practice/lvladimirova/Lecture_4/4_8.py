import random

lst = ("камень", "ножницы", "бумага")
computer = random.choice(lst)
print(computer)
user = str
while (user := input("Выберите камень, ножницы или бумагу. Или напишите 'хватит''!: ")).lower() != "хватит":
    computer = random.choice(lst)
    print(computer)
    if user in lst:
        if computer == user:
            print("Ничья, давай ещё!")
        if computer == "бумага" and user == "камень":
            print("Я победил тебя! Бумага заворачивает камень")
        if computer == "бумага" and user == "ножницы":
            print("Ножницы разрезали бумагу! Ой-ой, тебе просто повезло!")
        if computer == "ножницы" and user == "камень":
            print("Камень затупил ножницы! Ой-ой, тебе просто повезло!")
        if computer == "ножницы" and user == "бумага":
            print("Я победил тебя! Ножницы разрезали бумагу!")
        if computer == "камень" and user == "бумага":
            print("Бумага заворачивает камень! Ой-ой, тебе просто повезло!")
        if computer == "камень" and user == "ножницы":
            print("Я победил тебя! Камень затупил ножницы!")
    else:
        print("Внимательнее! Вводишь глупость!")
else:
    print("Спасибо за игру!")
