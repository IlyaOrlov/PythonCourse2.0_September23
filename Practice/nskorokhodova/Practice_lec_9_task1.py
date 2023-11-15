class ParagraphIterator:
    def __init__(self, text, paragraph_symbol):
        self.text = text
        self.paragraph_symbol = paragraph_symbol
        self.paragraphs = text.split(paragraph_symbol)
        self.current_paragraph = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.current_paragraph >= len(self.paragraphs):
            raise StopIteration

        paragraph = self.paragraphs[self.current_paragraph]
        self.current_paragraph += 1
        return paragraph.strip()

#  а если вообще через функцию это реализовать, а не через класс? это будет правильно?
def paragraph_iterator(text, paragraph_symbol):
    paragraphs = text.split(paragraph_symbol)

    for paragraph in paragraphs:
        yield paragraph


t = "Текст первого параграфа.Текст второго параграфа.Текст третьего параграфа."
symbol = "."

iterator = paragraph_iterator(t, symbol)

for paragraph in iterator:
    print(paragraph)
