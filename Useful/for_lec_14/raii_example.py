class RAIIExample:  # RAII
    def __init__(self):
        print("Begin")
        self._f = open("file.txt")

    def __del__(self):
        print("End")
        self._f.close()


x = RAIIExample()
print("Что-нибудь")
raise Exception()
