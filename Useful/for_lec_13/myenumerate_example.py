class MyEnumerate:
    def __init__(self, lst):
        self._lst = lst
        self._i = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self._i < len(self._lst):
            res = self._i, self._lst[self._i]
            self._i += 1
            return res

        raise StopIteration


lst1 = ["a", "b", "c", "d"]

for i, x in MyEnumerate(lst1):
     print(i, x)
