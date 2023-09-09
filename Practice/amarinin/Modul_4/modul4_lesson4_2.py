if __name__ == "__main__":
    number = input("Введите пятизначное число :  ")
    print(f"\nЧисло: {number}")
    for i, number_str in enumerate(number, 1):
        print(f"{i} цифра равна {number_str}")
