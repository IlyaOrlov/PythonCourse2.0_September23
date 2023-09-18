p = input("Введите слово: ")
while not p.isalpha():
    print("Ошибка! Вы ввели НЕ слово!")
    p = input("Попробуйте ещё раз: ")
p1 = p.lower()
p2 = p1[::-1]
res = p1 == p2
print(res)
