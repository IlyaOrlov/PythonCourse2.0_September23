ans = ("Ты сам-то понял, что написал?", "Аргументируй", "И?")
i = 0
while (x := input("Ваш запрос: ")) != "хватит":
    print(ans[i])
    if i < 2:
        i += 1
    else:
        i = 0
print("Ок")