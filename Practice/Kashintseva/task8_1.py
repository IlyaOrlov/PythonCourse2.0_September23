class Reader:
    def __init__(self, t, paragraf):
        self._t = t
        self._paragraf = paragraf
        self._i = 0

    def __iter__(self):
        return self

    def __next__(self):
        txt = ""
        while self._i < len(self._t):
            if self._t[self._i] == self._paragraf:
                txt += self._t[self._i]
                self._i += 1
                return txt
            txt += self._t[self._i]
            self._i += 1
        else:
            raise StopIteration


text = "Муха села\tНа варенье,\tВот и всё\tСтихотворение."
for n in Reader(text, "\t"):
    print(n)
