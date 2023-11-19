class ParagraphIterator:
    def __init__(self, st, ps):
        self.st = st
        self.ps = ps
        self.paragraphs = self.st.split(self.ps)
        self.current_paragraph = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.current_paragraph >= len(self.paragraphs):
            raise StopIteration
        else:
            paragraph = self.paragraphs[self.current_paragraph]
            self.current_paragraph += 1
            return paragraph


text = "Paragraph\n\nParagraph\n\nParagraph"
paragraph_separator = "\n\n"
paragraph_iterator = ParagraphIterator(text, paragraph_separator)
for p in paragraph_iterator:
    print(p.strip())
