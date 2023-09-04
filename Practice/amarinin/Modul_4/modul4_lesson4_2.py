if __name__ == "__main__":
    number = input("Введите пятизначное число :  ")
    if len(number) == 5 and number.isdecimal():
        print(f"\nЧисло: {number}")
        i = 1
        while i <= 5:
            number_str = number[i - 1]
            print(f"{i} цифра равна {number_str}")
            i += 1
    else:
        print(f"Вы ввели {number}  -  это не пятизначное число.")