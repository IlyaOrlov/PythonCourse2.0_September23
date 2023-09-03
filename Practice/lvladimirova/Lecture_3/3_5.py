s = input("Введите слово: ")
s1 = s.lower()
a = s1[0:]
b = s1[::-1]
if a == b:
    print(f"Слово палиндром! True")
else:
    print(f"Слово не палиндром! False")
