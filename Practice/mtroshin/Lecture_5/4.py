# def udalenie(s):
#     for i in lst1:
#         for d in i:
#             if int(s) == d:
#                 udal = i.index(d)
#                 for t in lst1:
#                     t.pop(udal)

def udalenie(s):
    n = int(s)  # чтоб не преобразовывать в цикле на каждой итерации
    for i in lst1:
        j = 0
        while j < len(i):
            if n == i[j]:
                for t in lst1:
                    t.pop(j)
            else:
                j += 1

lst1 = [[1, 2, 2], [4, 5, 6], [7, 8, 9]]
print("Изначальная матрица:\n")
for i in lst1:
    print(i)

s = input("\nВведите число: ")
udalenie(s)

print("\nМатрица после удаления столбца, содержащего введенную цифру:\n")
for i in lst1:
    print(i)