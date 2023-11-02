from itertools import filterfalse
lst = ['hello', 'i', 'write', 'cool', 'code']
res = filterfalse(lambda x: len(x) < 5, lst)
print(list(res))
