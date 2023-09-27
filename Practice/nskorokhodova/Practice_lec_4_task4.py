if __name__ == "__main__":
    otvet = ("Ты сам‐то понял, что написал?", "Аргументируй", "И?")
    x = 0
    while (y := input("Задай вопрос: ")).lower() != "хватит":
        print(otvet[x])
        if x < 2:
            x += 1
        else:
            x = 0
    else:
        print("Спор закончился!")
