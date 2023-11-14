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
        fat_duck = Ducks("Дейзи", self.weight + other.weight)
        return fat_duck


duck1 = Ducks("Скрудж", 10)
duck2 = Ducks("Билли", 5)
duck3 = Ducks("Вилли", 8)
duck4 = Ducks("Поночка", 6)
fat_duck = duck2 + duck4
duck1.voice()
Ducks.dcolor()
print(duck2)
print(repr(duck3))
print(duck4 > duck1)
print(duck2 < duck3)
print(duck1 == duck2)
print(duck3 != duck4)
print(fat_duck)
print(duck2.color)
