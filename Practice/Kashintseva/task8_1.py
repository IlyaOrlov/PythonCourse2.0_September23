class Reader:
    def __init__(self, t, paragraf):
        self._t = t
        self._paragraf = paragraf
        self._i = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self._i < len(self._t):
            txt = ""
            while self._i < len(self._t):
                y = self._t[self._i]
                txt += y
                self._i += 1
                if y == self._paragraf:
                    return txt
            else:
                return txt
        raise StopIteration


text = "Муха села\tНа варенье,\tВот и всё\tСтихотворение."
for n in Reader(text, "\t"):
    print(n)
