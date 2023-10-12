def udalenie(s):
    for i in lst1:
        for d in i:
            if int(s) == d:
                udal = i.index(d)
                for t in lst1:
                    t.pop(udal)


lst1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print("Изначальная матрица:\n")
for i in lst1:
    print(i)

s = input("\nВведите число: ")
udalenie(s)

print("\nМатрица после удаления столбца, содержащего введенную цифру:\n")
for i in lst1:
    print(i)