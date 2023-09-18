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
        elif computer == "бумага":
            if user == "камень":
                print("Я победил тебя! Бумага заворачивает камень")
            else:
                print("Ножницы разрезали бумагу! Ой-ой, тебе просто повезло!")
        elif computer == "ножницы":
            if user == "камень":
                print("Камень затупил ножницы! Ой-ой, тебе просто повезло!")
            else:
                print("Я победил тебя! Ножницы разрезали бумагу!")
        elif computer == "камень":
            if user == "бумага":
                print("Бумага заворачивает камень! Ой-ой, тебе просто повезло!")
            else:
                print("Я победил тебя! Камень затупил ножницы!")
    else:
        print("Внимательнее! Вводишь глупость!")
else:
    print("Спасибо за игру!")
