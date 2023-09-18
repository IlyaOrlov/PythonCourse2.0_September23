if __name__ == "__main__":
    s = str()
    while (x := input("Введите числовые символы: ")).lower() != "stop":
        if x.isdecimal():
            s += x
            print(s)
        else:
            print("Ошибка! Введено не число!")
    else:
        print(s)
