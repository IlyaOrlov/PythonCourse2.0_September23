class IterReadPar:
    def __init__(self, st, ps):
        self._st = st
        self._ps = ps
        self._i = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self._i < len(self._st):
            res = ""
            fl = 0
            while self._i < len(self._st):
                if self._st[self._i] == self._ps:
                    fl += 1
                if fl < 2:
                    if fl > 0:
                        res += self._st[self._i]
                    self._i += 1
                else:
                    break
            return res

        raise StopIteration


par_s = "&"
s = "& Paragraph 1.& Paragraph 2.& Paragraph 3."

for i in IterReadPar(s, par_s):
    print(i)
