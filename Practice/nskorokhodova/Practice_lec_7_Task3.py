class WrapStrToFile:
    def __init__(self):
        self._filepath = tempfile.mktemp()
        print(self._filepath)

    @property
    def content(self):
        try:
            with open(self._filepath, "r", encoding="utf-8") as file1:
                return file1.read()
        except FileNotFoundError:
            return 'File didnot exist'

    @content.setter
    def content(self, value):
        with open(self._filepath, "w", encoding="utf-8") as file1:
            file1.write(value)

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
