if __name__ == "__main__":
    s = input("Введите пятизначное число: ")
    if len(s) == 5 and s.isdecimal():
        print(f"Число:{s}")
        for i, x in enumerate(s, 1):
            print(f"{i} цифра равна {x}")
    else:
        print("Вы ввели не пятизначное число!")
