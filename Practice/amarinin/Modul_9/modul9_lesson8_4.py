import itertools


if __name__ == "__main__":
    print([a for a in itertools.chain([1, 2, 3], [4, 5], [6, 7])])
    print([a for a in itertools.filterfalse(lambda x: len(x) < 5, ["hello", "i", "write", "cool", "code"])])
    print([a for a in itertools.combinations('password', 4)])
