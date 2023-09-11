if __name__ == "__main__":
    s = input("Введите пятизначное число: ")
    if len(s) == 5:
        print(f"Число:{s}")
        for i, x in enumerate(s):
            if s[i].isdecimal():
                print(f"{i + 1} цифра равна {s[i]}")
                continue
    else:
        print("Вы ввели не пятизначное число!")
