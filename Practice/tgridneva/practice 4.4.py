answer = ("Ты сам-то понял, что написал?", "Аргументируй?", "И?")
i = 0
while (question := input("Введите Ваш вопрос: ")).lower() != "хватит":
    print(answer[i])
    if i < 2:
        i += 1
    else:
        i = 0
else:
    print(f"Конец программы! Хватит!")
