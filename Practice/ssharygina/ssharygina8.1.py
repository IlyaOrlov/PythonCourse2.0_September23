class ReadPar:
    def __init__(self, text, symbol):
        self.text = text
        self.symbol = symbol
        self.i = 0

    def __iter__(self):
        return self

    def __next__(self):
        par = ""
        while self.i < len(self.text):
            if self.text[self.i] == self.symbol:
                self.i += 1
                return par
            par += self.text[self.i]
            self.i += 1
        else:
            raise StopIteration


t1 = "Текст1.§Текст2.§Текст3.§"
s1 = "§"
r = ReadPar(t1, s1)
for p in r:
    print(p)
