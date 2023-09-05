if __name__ == "__main__":
    number = input("Введите пятизначное число :  ")
    print(f"\nЧисло: {number}")
    i = 1
    for number_str in number:
        print(f"{i} цифра равна {number_str}")
        i += 1
