if __name__ == "__main__":
    print("Попробуй меня переспорить! Скажи что-нибудь или 'Хватит'")
    otvet = ("Ты сам‐то понял, что написал?", "Аргументируй", "И?")
    i = 0
    while (x := input("Спрашивай или сдавайся: ")).lower() != "хватит":
        print(otvet[i])
        if i < 2:
            i += 1
        else:
            i = 0
    else:
        print("Что так быстро?")
