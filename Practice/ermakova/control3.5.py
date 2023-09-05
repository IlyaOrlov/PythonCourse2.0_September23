slovo = input("Введите слово: ").lower()
print(f"Является ли Ваше слово палиндромом? {slovo == slovo[::-1]}")
