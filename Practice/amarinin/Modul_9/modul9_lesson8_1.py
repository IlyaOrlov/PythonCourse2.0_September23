class Pager:
    def __init__(self, texts, separator):
        self.texts = texts + separator
        self.separator = separator
        self.i = 0

    def __iter__(self):
        return self

    def __next__(self):
        try:
            if self.i < len(self.texts):
                paragraph = ""
                while True:
                    if self.texts[self.i] == self.separator:
                        self.i += 1
                        return paragraph
                    else:
                        paragraph += self.texts[self.i]
                    self.i += 1
            raise StopIteration
        except IndexError:
            print("100 % ! поставили в качестве разделителя '' или еще какую то ерунду")
            exit()
        except TypeError:
            print("Будьте внимательны")


if __name__ == "__main__":
    text = "12311\t2222\t3333\t4444\t5555\t666"
    a = Pager(text, "\t")
    for i in a:
        if input("Читаем ? Y/N : ").upper() == "Y":
            print(f"{chr(167)}  {i}")
        else:
            break

        # не нравится почему то пайтону else break в конце строчки (
        # print(f"{chr(167)}   {i}") if input("Читаем ? Y/N : ").upper() == "Y" else break
