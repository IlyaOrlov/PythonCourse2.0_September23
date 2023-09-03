s = input("Введите слово: ")
a = s[0:]
b = s[::-1]
if a == b:
    print(f"Слово палиндром! True")
else:
    print(f"Слово не палиндром! False")
