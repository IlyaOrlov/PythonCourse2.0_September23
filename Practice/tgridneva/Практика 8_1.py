class ParagraphReader:
    def __init__(self, text, symbol):
        self._text = text
        self._symbol = symbol
        self._i = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self._i >= len(self._text):
            raise StopIteration

        start = self._i
        while self._i < len(self._text) and self._text[self._i] != self._symbol:
            self._i += 1

        paragraph = self._text[start:self._i]
        self._i += 1

        return paragraph


text = "This is the first paragraph.\n\nThis is the second paragraph.\n\nThis is the third paragraph."

reader = ParagraphReader(text, symbol='\n')

for paragraph in reader:
    print(paragraph)
