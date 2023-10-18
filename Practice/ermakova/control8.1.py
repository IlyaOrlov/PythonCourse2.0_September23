class Read:
    def __init__(self, text, symbol):
        self.text = text
        self.symbol = symbol
        self.i = 0
        self.txt = ""

    def __iter__(self):
        return self

    def __next__(self):
        paragraph = ""
        while self.i < len(self.text):
            self.txt = ""
            if self.text[self.i] == self.symbol:
                self.txt += paragraph
                self.i += 1
                return self.txt
            paragraph += self.text[self.i]
            self.i += 1
        else:
            raise StopIteration


text1 = "Привет1.§Привет2.§Привет3.§"
symbol1 = "§"
r = Read(text1, symbol1)
for p in r:
    print(p)
