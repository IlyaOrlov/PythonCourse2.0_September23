class ParagraphIterator:
    def __init__(self, text, paragraph_separator):
        self.paragraphs = text.split(paragraph_separator)
        self.current_paragraph = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.current_paragraph < len(self.paragraphs):
            paragraph = self.paragraphs[self.current_paragraph]
            self.current_paragraph += 1
            return paragraph
        else:
            raise StopIteration


text = "первый.§второй.§третий"

paragraph_separator = "§"

iter_paragraphs = ParagraphIterator(text, paragraph_separator)

for paragraph in iter_paragraphs:
    print(paragraph.strip())