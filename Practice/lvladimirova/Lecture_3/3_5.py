s = input("Введите слово: ")
s1 = s.lower()
if s1 == s1[::-1]:
    print(f"Слово палиндром! True")
else:
    print(f"Слово не палиндром! False")
