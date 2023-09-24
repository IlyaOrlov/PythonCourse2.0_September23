if __name__ == "__main__":
    x = input("Введите число из 5 цифр: ")
    if len(x) == 5 and x.isdecimal():
        print(f"Число:{x}")
        for i, x in enumerate(x, 1):
            print(f"{i} цифра равна {x}")
    else:
        print("Вы ввели не пятизначное число!")