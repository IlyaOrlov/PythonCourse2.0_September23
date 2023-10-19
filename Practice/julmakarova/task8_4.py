import itertools


s = itertools.chain([1, 2, 3], [4, 5], [6, 7])
lst = [x for x in s]
print(lst)

s2 = itertools.filterfalse(lambda x: len(x) < 5, ['hello', 'i', 'write', 'cool', 'code'])
lst2 = [x for x in s2]
print(lst2)

s3 = itertools.combinations("password", 4)
lst3 = [x for x in s3]
print(lst3)
