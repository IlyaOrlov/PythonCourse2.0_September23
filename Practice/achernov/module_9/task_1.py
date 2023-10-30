class MyIter:

    def __init__(self, text, my_paragraph):
        self._text = text
        self._paragraph = my_paragraph
        self._i = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self._i < len(self._text):
            res = ""
            while self._i < len(self._text):
                x = self._text[self._i]
                res += x
                self._i += 1
                if x == self._paragraph:
                    return res
            else:
                return res
        raise StopIteration


my_text = "§1.Сначала печатается это. \nЭто ктстати тоже. \n§2.Тут тоже должно напечаться"
paragraph = "§"
my_iter = MyIter(my_text, paragraph)
for n in my_iter:
    print(n)
