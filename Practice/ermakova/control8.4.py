import itertools

print([x for x in itertools.chain([1, 2, 3], [4, 5], [6, 7])])

print([x for x in itertools.filterfalse(lambda x: len(x) < 5, ['hello', 'i', 'write', 'cool', 'code'])])

lst2 = list(itertools.combinations("password", 4))
print(lst2)
