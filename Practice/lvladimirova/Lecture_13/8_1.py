class Reader:
    def __init__(self, text, par):
        self._text = text
        self._par = par
        self._i = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self._i < len(self._text):
            x = ""
            while self._i < len(self._text):
                y = self._text[self._i]
                x += y
                self._i += 1
                if y == self._par:
                    return x
            else:
                return x
        raise StopIteration


if __name__ == "__main__":
    my_text = "Как\tхорошо\tуметь\tчитать"
    for n in Reader(my_text, "\t"):
        print(n)
