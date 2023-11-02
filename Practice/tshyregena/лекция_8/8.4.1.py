from collections.abc import Iterable


def flatten(items: Iterable):
    for item in items:
        if isinstance(item, Iterable):
            yield from flatten(item)
        else:
            yield item


items1 = ([1, 2, 3], [4, 5], [6, 7])
print(list(flatten(items1)))
