class Duck:
    color = "желтый"

    def __init__(self, name, weight):
        self.name = name
        self.weight = weight

    @staticmethod
    def crack():
        print(f"Сrack")

    @classmethod
    def color_duck(cls):
        print(f"Цвет наших уток {cls.color}!")

    def info(self):
        print(f"Уточка {self.name} весит {self.weight} кг.")
        Duck.crack()

    def __repr__(self):
        return f"Утка {id(self)} под именем {self.name} весит {self.weight}."

    def __gt__(self, other):
        return self.weight > other.weight

    def __lt__(self, other):
        return self.weight < other.weight

    def __eq__(self, other):
        return self.weight == other.weight

    def __ne__(self, other):
        return self.weight != other.weight

    def __add__(self, other):
        new_weight = self.weight + other.weight
        new_duck = Duck("Крошка", new_weight)
        return new_duck


d1 = Duck("Кря-кря", 10)
d2 = Duck("Ку-ку", 5)
d3 = Duck("Пи-пи", 5)

d1.info()
d2.info()
d2.info()
print(repr(d1))
print(repr(d2))
Duck.color_duck()
print(f"Утка {d1.name} больше весит чем {d2.name}:{d1 > d2}")
print(f"Утка {d1.name} меньше весит чем {d2.name}:{d1 < d2}")
print(f"Утки {d2.name} и {d3.name} одинаково весят:{d2 == d3}")
print(f"Утки {d2.name} и {d3.name} одинаково весят:{d2 != d3}")
d0 = d1 + d2
d0.info()
