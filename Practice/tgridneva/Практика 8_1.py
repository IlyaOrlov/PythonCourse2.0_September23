class ParagraphIterator:
    def __init__(self, text1, paragraph_symbol):
        self.text = text1
        self.paragraph_symbol = paragraph_symbol
        self.paragraphs = self.text.split(self.paragraph_symbol)
        self.current_paragraph = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.current_paragraph < len(self.paragraphs):
            par = self.paragraphs[self.current_paragraph]
            self.current_paragraph += 1
            return par.strip()
        else:
            raise StopIteration


text = "This is the first paragraph.##This is the second paragraph.##And this is the third paragraph."

paragraph_iterator = ParagraphIterator(text, "##")

for paragraph in paragraph_iterator:
    print(paragraph)
