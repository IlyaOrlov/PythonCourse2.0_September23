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
            while self._i < len(self._st):
                if self._st[self._i] == self._ps:
                    self._i += 1
                    break
                else:
                    res += self._st[self._i]
                    self._i += 1
            return res

        raise StopIteration


par_s = "p"
s = "p Paragraf 1. p Paragraf 2. p Paragraf 3."

for i in IterReadPar(s, par_s):
    print(i)
