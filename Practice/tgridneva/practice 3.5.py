palindrom = input("Введите слово: ")
if str(palindrom) == str(palindrom)[::-1]:
    print("True")
else:
    print("False")
