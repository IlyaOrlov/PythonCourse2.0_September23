import random
while True:
    a = round(random.uniform(1,3))
    print ("1 - камень","2 - ножницы","3 - бумага", sep='\n')
    p = int(input())
    res = ("камень", "ножницы", "бумага")
    print(f"Компьютер выбрал {res[a - 1]}")
    if a == p:
        print("Ничья")
    if a == 1 and p==2:
        print("Вы проиграли")
    if a == 1 and p==3:
        print("Вы выйграли!")
    if a == 2 and p==1:
        print("Вы выйграли!")
    if a == 2 and p==3:
        print("Вы проиграли")
    if a == 3 and p==1:
        print("Вы проиграли")
    if a == 3 and p==2:
        print("Вы выйграли!")
    qw = input("Начать заново? (да\нет) ")
    if qw == 'нет':
        break
