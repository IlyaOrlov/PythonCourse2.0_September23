import itertools


lst1 = itertools.chain([1, 2, 3], [4, 5], [6, 7])
lst2 = [x for x in lst1]
print(lst2)
print("*******************************************************")
lst3 = itertools.filterfalse(lambda x: len(x) < 5, ["hello", "i", "write", "cool", "code"])
lst4 = [x for x in lst3]
print(lst4)
print("*******************************************************")
s1 = itertools.combinations("password", 4)
lst5 = [x for x in s1]
print(lst5)
