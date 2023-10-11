import tempfile
import os


class WrapStrToFile:
    def __init__(self):
        self._filepath = tempfile.mkstemp()

    @property
    def content(self):
        try:
            with open(self._filepath, "r", encoding="utf-8") as file1:
                return file1.read()
        except FileNotFoundError:
            return 'File doesnt exist'

    @content.setter
    def content(self, value):
            with open(self._filepath, "w", encoding="utf-8") as file1:
                file1.write(value)

    @content.deleter
    def content(self):
        os.remove(self._filepath)


wstf = WrapStrToFile()
print(wstf.content)  # Output: File doesn't exist
wstf.content = 'test str'
print(wstf.content)  # Output: test_str
wstf.content = 'text 2'
print(wstf.content)  # Output: text 2
del wstf.content
