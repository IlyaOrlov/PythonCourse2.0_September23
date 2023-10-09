import tempfile
import os


class WrapStrToFile:
    def __init__(self):
        self._filepath = tempfile.mktemp()

    @property
    def content(self):
        try:
            with open(self._filepath, 'r') as file:
                return file.read()
        except FileNotFoundError:
            return 'Файл еще не существует'

    @content.setter
    def content(self, value):
        with open(self._filepath, 'w') as file:
            file.write(value)

    @content.deleter
    def content(self):
        try:
            os.remove(self._filepath)
        except FileNotFoundError:
            pass


wrapper = WrapStrToFile()
print(wrapper.content)

wrapper.content = "Hello, world!"
print(wrapper.content)

del wrapper.content
print(wrapper.content)
