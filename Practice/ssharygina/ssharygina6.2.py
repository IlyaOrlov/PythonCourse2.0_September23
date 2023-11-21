class Duck:
    color = "желтый"

    def __init__(self, name, weight):
        self.name = name
        self.weight = weight

    @staticmethod
    def say_crack():
        print(f"Сrack")

    @classmethod
    def color_duck(cls):
        print(f"Цвет всех уток {cls.color}!")

    def info(self):
        print(f"Утка {self.name} весит {self.weight} кг.")

    def __repr__(self):
        return f"Утка {self.name}. Вес: {self.weight} кг."

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
        return Duck("СуперУтка", new_weight)


d1 = Duck("Яна", 8)
d2 = Duck("Поля", 3)
d3 = Duck("Надя", 5)
d1.info()
d2.info()
d3.info()
print(repr(d1))
print(repr(d2))
print(repr(d3))
d1.say_crack()
Duck.color_duck()
print(f"Вес утки {d1.name} больше, чем вес утки {d2.name}: {d1 > d2}")
print(f"Вес утки {d2.name} меньше, чем вес утки {d3.name}: {d2 < d3}")
print(f"Утки {d2.name} и {d3.name} одинаково весят: {d2 == d3}")
print(f"Вес утки {d2.name} не равен весу утки {d3.name}: {d2 != d3}")
d = d1 + d2
d.info()
