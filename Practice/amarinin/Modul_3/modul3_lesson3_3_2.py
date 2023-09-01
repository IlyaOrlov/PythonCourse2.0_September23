if __name__ == "__main__":
    key_parole = int(input("Введите зашифрованный цифровой пароль (целое число) : "))
    key = int(input("Введите секретный код   (целое число)               : "))
    password = key_parole ^ key
    print(f"\nЦифровой пароль   {password}")
