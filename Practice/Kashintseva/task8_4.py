import os
import itertools


def combine(m):
    c = list(itertools.chain.from_iterable(m))
    return c


def word(s):
    p = list(itertools.filterfalse(lambda x: len(x) < 5, s))
    return p


def diff(y):
    d = list(itertools.combinations_with_replacement(y, 4))
    return d


a = ([1, 2, 3], [4, 5], [6, 7])
print(combine(a))
b = (['hello', 'i', 'write', 'cool', 'code'])
print(word(b))
z = 'password'
print(diff(z))
