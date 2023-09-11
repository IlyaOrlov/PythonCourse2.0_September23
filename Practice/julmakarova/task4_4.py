req = input("Введите запрос: ")
ans = ["Ты сам-то понял, что написал?", "Аргументируй", "И?"]
counter = 0
while req != "хватит":
    print(ans[counter])
    req = input("Введите новый запрос: ")
    if counter == 2:
        counter = 0
    else:
        counter += 1
