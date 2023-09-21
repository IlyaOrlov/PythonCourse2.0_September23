import random


xyz = ("камень", "ножницы", "бумага")
computer = random.choice(xyz)
print(computer)
user = str
while (user := input("Выберите камень, ножницы или бумагу. Или напишите 'хватит''!: ")).lower() != "хватит":
    computer = random.choice(xyz)
    print(computer)
    if user in xyz:
        if computer == user:
            print("Ничья, выбери еще: камень, ножницы, бумага")
        elif computer == "бумага":
            if user == "камень":
                print("Победа! Бумага заворачивает камень")
            else:
                print("Ножницы разрезали бумагу! извини)))")
        elif computer == "ножницы":
            if user == "камень":
                print("Камень точит ножницы!")
            else:
                print("Победа! Ножницы разрезали бумагу!")
        elif computer == "камень":
            if user == "бумага":
                print("Бумага заворачивает камень!")
            else:
                print("Победа! Камень точит ножницы!")
    else:
        print("Внимательнее, что-то ввел неправильное!")
else:
    print("Спасибо, игра окончена!")
