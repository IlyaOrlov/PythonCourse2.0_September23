class ParagraphReader:
    def __init__(self, text):
        self._text = text
        self._paragraphs = []

    def read_paragraphs(self):
        paragraph = ''
        for char in self._text:
            if char == '\n':
                if paragraph:
                    self._paragraphs.append(paragraph)
                    paragraph = ''
            else:
                paragraph += char
        if paragraph:
            self._paragraphs.append(paragraph)
        return self._paragraphs


text = "This is the first paragraph.\n\nThis is the second paragraph.\n\nThis is the third paragraph."

reader = ParagraphReader(text)
paragraphs = reader.read_paragraphs()

for paragraph in paragraphs:
    print(paragraph)
