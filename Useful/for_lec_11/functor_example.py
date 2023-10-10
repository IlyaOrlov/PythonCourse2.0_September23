class Multiplier:
    def __init__(self, base):
        self.base = base
        self.history = []

    def __call__(self, num):
        self.history.append(num)
        return self.base + num


m = Multiplier(10)
print(m(50))
print(m(20))
print(m.history)
