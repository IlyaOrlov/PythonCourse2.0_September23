import random
while True:
    a = round(random.randint(1,3))
    print ("1 - камень","2 - ножницы","3 - бумага", sep='\n')
    p = input("Введите число от 1 до 3: ")

    if p not in ["1", "2", "3"]:
        print("Ошибка!Нужно ввести число от 1 до 3")
    else:
        p = int(p)
        res = ("камень", "ножницы", "бумага")
        print(f"Компьютер выбрал {res[a - 1]}")
        if a == p:
            print("Ничья")
        elif a == 1 and p==2:
            print("Вы проиграли")
        elif a == 1 and p==3:
            print("Вы выйграли!")
        elif a == 2 and p==1:
            print("Вы выйграли!")
        elif a == 2 and p==3:
            print("Вы проиграли")
        elif a == 3 and p==1:
            print("Вы проиграли")
        elif a == 3 and p==2:
            print("Вы выйграли!")
    qw = input("Начать заново? (да\нет) ")
    if qw == 'нет':
        break
