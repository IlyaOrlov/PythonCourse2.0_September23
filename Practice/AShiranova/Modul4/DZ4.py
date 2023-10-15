answer = ["Ты сам-то понял что написал?", "Аргументируй", "И"]
counter = 0
while (req := input("Введите запрос: ")) != "хватит":
    print(answer[counter])
    if counter == 2:
        counter = 0
    else:
        counter += 1
