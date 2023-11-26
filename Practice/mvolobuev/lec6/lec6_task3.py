# WrapStrFlle
import tempfile
import os


class WrapStrToFile:
    def __init__(self):
        self.filepach = tempfile.mktemp()

    @property
    def content(self):
        try:
            with open(self.filepach, "r", encoding="utf-8") as f1:
                return f1.read()
        except FileNotFoundError as e:
            print(e)
            return "File doesn't exist"

    @content.setter
    def content(self, value):
        with open(self.filepach, "w", encoding="utf-8") as f1:
            f1.write(value)

    @content.deleter
    def content(self):
        os.remove(self.filepach)
        print("Файл удален")


wstf = WrapStrToFile()
print(wstf.content)
wstf.content= "test str"
print(wstf.content)
wstf.content = "text 2"
print(wstf.content)
del wstf.content  # после этого файла не существует
