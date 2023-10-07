class Ducks:
    color = "yellow"

    def __init__(self, name, weight):
        self.name = name
        self.weight = weight

    @staticmethod
    def voice():
        print("Crack")

    @classmethod
    def dcolor(cls):
        print(f"Цвет уток: {cls.color}")

    def __str__(self):
        return f"Имя утки: {self.name}, вес утки: {self.weight}"

    def __repr__(self):
        return f"Имя утки с номером {id(self)}: {self.name}, вес утки: {self.weight}"

    def __gt__(self, other):
        return self.weight > other.weight

    def __lt__(self, other):
        return self.weight < other.weight

    def __eq__(self, other):
        return self.weight == other.weight

    def __ne__(self, other):
        return self.weight != other.weight

    def __add__(self, other):
        return self.weight + other.weight


duck1 = Ducks("Дональд", 10)
duck2 = Ducks("Тина", 5)
duck3 = Ducks("Толик", 8)
duck4 = Ducks("Роза", 6)
bigduck = duck2 + duck4
duck1.voice()
Ducks.dcolor()
print(duck2)
print(repr(duck3))
print(duck4 > duck1)
print(duck2 < duck3)
print(duck1 == duck2)
print(duck3 != duck4)
print(bigduck)
