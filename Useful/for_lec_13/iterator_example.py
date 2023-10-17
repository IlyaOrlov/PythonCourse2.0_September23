class Nums:
    def __init__(self, limit):
        self._limit = limit
        self._i = 2
        self._num = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self._num < self._limit:
            res = self._i
            self._i += 2
            self._num += 1
            return res

        raise StopIteration


for i in Nums(10):
    print(i)


# n = Nums(10)
# it = iter(n)
# while True:
#     try:
#         print(next(it))
#     except StopIteration:
#         break
