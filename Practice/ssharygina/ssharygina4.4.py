zapr = input("Введите запрос: ")
otv = ["Ты сам-то понял, что написал?", "Аргументируй", "И?"]
rob = 0
while zapr != "хватит":
    print(otv[rob])
    zapr = input("Введите новый запрос: ")
    if rob == 2:
        rob = 0
    else:
        rob += 1
