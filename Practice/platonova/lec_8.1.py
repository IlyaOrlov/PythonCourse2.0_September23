class ParagraphIterator:
    def __init__(self, text, paragraph_symbol):
        self.text = text
        self.paragraph_symbol = paragraph_symbol
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index == len(self.text):
            raise StopIteration

        buffer = ''

        while self.index < len(self.text):
            char = self.text[self.index]

            if char == self.paragraph_symbol:
                self.index += 1
                return buffer.strip()

            buffer += char
            self.index += 1

        return buffer.strip()


text = "Это первый параграф. §А это второй параграф. §А это третий параграф"
symbol = '§'

paragraph_iterator = ParagraphIterator(text, symbol)
for paragraph in paragraph_iterator:
    print(paragraph)
