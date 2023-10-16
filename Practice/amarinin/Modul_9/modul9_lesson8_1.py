class Pager:
    def __init__(self, texts, separator):
        self.texts = texts + separator
        self.paragraph = ""
        self.separator = separator

    def __iter__(self):
        return self

    def __next__(self):
        n = 1
        for char in self.texts:
            if char == self.separator:
                read = input("Читаем ? Y/N : ").upper()
                if read == "Y":
                    print(f"{chr(167)}{n} {self.paragraph}")
                    self.paragraph = ""
                    n += 1
                else:
                    break
            else:
                self.paragraph = self.paragraph + char
        raise StopIteration


if __name__ == "__main__":
    text = "12\t3456\t444\t55555"
    a = Pager(text, "\t")
    for i in a:
        print(i)
