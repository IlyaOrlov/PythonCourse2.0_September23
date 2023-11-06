class Duck:
    color = "Желтый"

    def __init__(self, name, weight):
        self.name = name
        self.weight = weight

    @classmethod
    def color_p(cls):
        print(f"Цвет утки {cls.color}")

    def print_p(self):
        print(f"Имя - {self.name}. Вес {self.weight} кг")

    @staticmethod
    def say_crack():
        print('Crack')

    def __lt__(self, other):
        return self.weight < other.weight

    def __ne__(self, other):
        return self.weight != other.weight

    def __eq__(self, other):
        return self.weight == other.weight

    def __add__(self, other):
        new_weight = self.weight + other.weight
        new_duck = Duck("Билли", new_weight)
        return new_duck

    def __repr__(self):
        return f"Duck  in {id(self)}: {self.name=}, {self.weight=}"


d = Duck("Дилли", 1.2)
d.print_p()
d.say_crack()
d1 = Duck("Вилли", 2)
d1.print_p()
d1.say_crack()
Duck.color_p()
print(d > d1)
print(d < d1)
print(d1 == d1)
s = d + d1
print(s.weight)
print(repr(s))
