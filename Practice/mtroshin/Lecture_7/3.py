import os
import tempfile

class WrapStrToFile:
    def __init__(self):
        # здесь инициализируется атрибут filepath, он содержит путь до файла-хранилища
        self._filepath = tempfile.mktemp()
        print(self._filepath)


    @property
    def content(self):
        try:
            with open(self._filepath, "r", encoding="utf-8") as file1:
                return file1.read()
        except FileNotFoundError:
            return "File doesn't exist"

    @content.setter
    def content(self, value):
        with open(self._filepath, "w", encoding="utf-8") as file1:
            file1.write(value)

    @content.deleter
    def content(self):
        os.remove(self._filepath)
        # удаляем файл: os.remove(имя_файла)


wstf = WrapStrToFile()
print(wstf.content)  # Output: File doesn't exist
wstf.content = 'test str'
print(wstf.content)  # Output: test_str
wstf.content = 'text 2'
print(wstf.content)  # Output: text 2
del wstf.content     # после этого файла не существует