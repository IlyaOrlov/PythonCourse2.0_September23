slovo1 = input("Введите слово: ").lower()
slovo2 = slovo1[::-1]
res = slovo1 == slovo2
print(f"Данное слово является палиндромом?\n {res}")
