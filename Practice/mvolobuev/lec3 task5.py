slovo = input("Введите слово полиндром :  ")
z1 = slovo.lower()
z2 = z1.strip()
z3 = z2
z3 = z3[::-1]
if z2 == z3:
    print("True")
else:
    print("False")
