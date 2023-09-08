palindrom = input("Введите слово: ").lower().replace(' ', '')
print(palindrom == palindrom[::-1])
