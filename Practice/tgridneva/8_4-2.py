import itertools


def filter_strings(strings):
    return list(itertools.filterfalse(lambda s: len(s) < 5,strings))


input_strings = ['hello', 'i', 'write', 'cool', 'code']
result = filter_strings(input_strings)
print(result)
