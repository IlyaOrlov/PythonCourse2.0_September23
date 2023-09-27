if __name__ == "__main__":
    x = str()
    while (y := input("Введите числовые символы: ")).lower() != "stop":
        if y.isdecimal():
            x += y
            print(x)
        else:
            print("Error!!! Введите число!")
    else:
        print(x)
