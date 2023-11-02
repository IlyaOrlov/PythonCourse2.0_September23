class Par:
    def __init__(self, text, p):
        self.text = text
        self.p = p
        self.i = 0

    def __iter__(self):
        return self

    def __next__(self):
        res = ""
        while self.i < len(self.text):
            res1 = self.i
            self.i += 1
            if self.text[res1] != self.p:
                res += self.text[res1]
            else:
                return res
        if res:
            return res
        raise StopIteration


t = Par("Египетская летучая §собака имеет длину §примерно 17 см", "§")
it = iter(t)
while True:
    try:
        print(next(it))
    except StopIteration:
        break
