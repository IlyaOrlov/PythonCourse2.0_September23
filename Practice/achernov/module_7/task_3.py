import os
import tempfile


class WrapStrToFile:

    def __init__(self):
        self._filepath = tempfile.mktemp()

    @property
    def content(self):
        try:
            with open(self._filepath, "r") as file:
                return file.read()
        except FileNotFoundError:
            print("Файл ещё не существует")

    @content.setter
    def content(self, value):
        with open(self._filepath, "w") as file:
            file.write(value)

    @content.deleter
    def content(self):
        os.remove(self._filepath)


wstf = WrapStrToFile()
print(wstf.content)
wstf.content = 'test str'
print(wstf.content)
wstf.content = 'text 2'
print(wstf.content)
del wstf.content
