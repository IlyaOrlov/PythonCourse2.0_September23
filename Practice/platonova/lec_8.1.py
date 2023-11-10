class ParagraphIterator:
    def __init__(self, text, paragraph_symbol):
        self.text = text
        self.paragraph_symbol = paragraph_symbol
        self.buffer = ''
        self.i = 0

    def __iter__(self):
        return self

    def __next__(self):
        while self.i < len(self.text):
            if self.text[self.i] == self.paragraph_symbol:
                result = self.buffer
                self.buffer = ''
                self.i += 1
                return result
            else:
                self.buffer += self.text[self.i]
                self.i += 1

        if self.buffer != '':
            result = self.buffer
            self.buffer = ''
            return result

        raise StopIteration()



text = 'Это первый параграф. §А это второй параграф. §А это третий параграф.'

iterator = ParagraphIterator(text, '§')

for paragraph in iterator:
    print(paragraph)
