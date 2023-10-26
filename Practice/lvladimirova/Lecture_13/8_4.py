import itertools

if __name__ == "__main__":
    s1 = itertools.chain([1, 2, 3], [4, 5], [6, 7])
    lst1 = [x for x in s1]
    print(lst1)
    print("===========================")
    s2 = itertools.filterfalse(lambda x: len(x) < 5, ['hello', 'i', 'write', 'cool', 'code'])
    lst2 = [x for x in s2]
    print(lst2)
    print("===========================")
    s3 = itertools.combinations("password", 4)
    lst3 = [x for x in s3]
    print(lst3)
