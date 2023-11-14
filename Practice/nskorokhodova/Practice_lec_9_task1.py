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
