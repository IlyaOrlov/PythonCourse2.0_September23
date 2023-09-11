def choice(name):
    return input(f"{name}, выберите k (камень), n (ножницы) или b (бумагу): ")


k = "камень"
n = "ножницы"
b = "бумага"
name1 = input("Введите имя первого игрока: ")
name2 = input("Введите имя второго игрока: ")
while (u1 := choice(name1)) == (u2 := choice(name2)):
    print("Ничья. Сделайте новый выбор!")
else:
    if u1 == "k":
        if u2 == "n":
            print(f"Победитель {name1}. Поздравляем!")
        else:
            print(f"Победитель {name2}. Поздравляем!")
    elif u1 == "n":
        if u2 == "k":
            print(f"Победитель {name2}. Поздравляем!")
        else:
            print(f"Победитель {name1}. Поздравляем!")
    elif u1 == "b":
        if u2 == "k":
            print(f"Победитель {name1}. Поздравляем!")
        else:
            print(f"Победитель {name2}. Поздравляем!")
    else:
        print("Некорректный ввод.")
