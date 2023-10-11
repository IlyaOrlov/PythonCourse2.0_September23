class Duck:
    color = "коричневый"

    def __init__(self, name, weight):
        self.name = name
        self.weight = weight

    @classmethod
    def color_p(cls):
        print(f"Цвета уток в корзинке {cls.color}")

    def print_p(self):
        print(
            f"Я вешу {self.weight} грамм. Меня зовут {self.name}")

    @staticmethod
    def say_crack():
        print('Crack')

    def __gt__(self, other):
        return self.weight > other.weight

    def __lt__(self, other):
        return self.weight < other.weight

    def __ne__(self, other):
        return self.weight != other.weight

    def __eq__(self, other):
        return self.weight == other.weight

    def __add__(self, other):
        new_weight = self.weight + other.weight
        new_duck = Duck("Шпуня", new_weight)
        return new_duck

    def __repr__(self):
        return f"Duck at {id(self)}: {self.name=}, {self.weight=}"


d = Duck("Minimi", 100)
d.print_p()
d.say_crack()
d1 = Duck("Minily", 90)
d1.print_p()
d1.say_crack()
d2 = Duck("Roma", 150)
d2.print_p()
d2.say_crack()
d3 = Duck("Fufa", 190)
d3.print_p()
d3.say_crack()
Duck.color_p()
print(d > d2)
print(d1 < d2)
print(d3 != d3)
print(d2 == d2)
s = d1 + d3
print(s.weight)
print(repr(s))
