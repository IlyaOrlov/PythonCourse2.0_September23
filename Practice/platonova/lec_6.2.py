class Duck:
    color = "Желтый"

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
        return f"Имя утки с id-номером {id(self)}: {self.name}, вес утки: {self.weight}"

    def __lt__(self, other):
        return self.weight < other.weight

    def __gt__(self, other):
        return self.weight > other.weight

    def __eq__(self, other):
        return self.weight == other.weight

    def __ne__(self, other):
        return self.weight != other.weight

    def __add__(self, other):
        sum_duck = Duck(None, self.weight + other.weight)
        return sum_duck


duck1 = Duck("Саша", 1)
duck2 = Duck("Петя", 2)
sum_duck = duck1 + duck2
duck1.voice()
Duck.dcolor()
print(duck2)
print(repr(duck1))
print(duck1 > duck2)
print(duck1 < duck2)
print(duck1 == duck2)
print(duck1 != duck2)
print(sum_duck)
print(duck2.color)