if __name__ == "__main__":

    word = input("Введите слово  : ")
    revers_word = word[::-1]
    polindrom = (word == revers_word)
    print(f"Ваше слово полиндром?  {polindrom}  !!!")
