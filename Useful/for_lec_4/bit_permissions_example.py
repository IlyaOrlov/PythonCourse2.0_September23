permissions = int(input("Введите ваш уровень доступа: "))
if permissions > 7:
    print("Некорректный уровень: ")
else:
    print(f"R|W|E = {permissions:b}")
