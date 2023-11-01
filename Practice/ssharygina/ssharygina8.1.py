class ReadPar:
    def __init__(self, text, symbol):
        self._text = text
        self._symbol = symbol
        self._i = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self._i < len(self._text):
            par = ""
            while self._i < len(self._text):
                x = self._text[self._i]
                par += x
                self._i += 1
                if x == self._symbol:
                    return par
            else:
                return par
        raise StopIteration


t1 = "§1Текст1.§2Текст2.\nТекст3.§3Текст4."
s1 = "§"
r = ReadPar(t1, s1)
for p in r:
    print(p)
