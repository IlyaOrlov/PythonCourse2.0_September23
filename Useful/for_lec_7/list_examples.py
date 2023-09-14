lst = [1, 2, 3, 4, 5]

lst1 = []
for i in lst:
    if i % 2 == 0:
        lst1.append(i * i)
    else:
        lst1.append("*")
print(lst1)

lst2 = [i * i if i % 2 == 0 else "*" for i in lst]
print(lst2)

