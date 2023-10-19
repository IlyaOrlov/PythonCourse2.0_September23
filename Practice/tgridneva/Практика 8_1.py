class ParagraphReader:
    def __init__(self, text):
        self._text = text
        self._buffer = []

    def read_paragraphs(self):
        paragraphs = []
        for char in self._text:
            if char == '\n':
                if self._buffer:
                    paragraph = ''.join(self._buffer)
                    paragraphs.append(paragraph)
                    self._buffer = []
            else:
                self._buffer.append(char)
        if self._buffer:
            paragraph = ''.join(self._buffer)
            paragraphs.append(paragraph)
        return paragraphs


text = "This is the first paragraph.\n\nThis is the second paragraph.\n\nThis is the third paragraph."

reader = ParagraphReader(text)
paragraphs = reader.read_paragraphs()

for paragraph in paragraphs:
    print(paragraph)
