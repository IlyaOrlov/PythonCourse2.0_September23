slovo = input("Введите слово полиндром :  ")
z = slovo.lower().strip()
print(z == z[::-1])
