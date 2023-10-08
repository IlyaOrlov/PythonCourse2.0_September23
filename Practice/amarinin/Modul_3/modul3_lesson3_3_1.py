if __name__ == "__main__":
    password = int(input("Введите цифровой пароль (целое число) : "))
    key = int(input("Введите секретный код   (целое число) : "))
    key_parole = password ^ key
    print(f"\nЗашифрованный цифровой пароль   {key_parole}")
