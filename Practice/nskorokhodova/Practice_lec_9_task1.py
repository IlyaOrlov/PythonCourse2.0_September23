class ParagraphIterator:
    def __init__(self, text, paragraph_separator):
        self.text = text
        self.paragraph_separator = paragraph_separator
        self.paragraphs = self.text.split(self.paragraph_separator)
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= len(self.paragraphs):
            raise StopIteration
        else:
            paragraph = self.paragraphs[self.index]
            self.index += 1
            return paragraph


text = """
В лесу родилась елочка. В лесу она росла.
Зимой и летом стройная.
Зеленая была.
"""

paragraph_separator = '.'
paragraphs = ParagraphIterator(text, paragraph_separator)

for paragraph in paragraphs:
    print(paragraph)