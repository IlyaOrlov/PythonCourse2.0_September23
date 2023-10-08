class Duck:
    color = "yellow"

    def __init__(self, name, weight):
        self.name = name
        self.weight = weight

    @staticmethod
    def print_crack():
        print("Crack")

    @classmethod
    def print_color(cls):
        print(f"{cls.color}")

    def print_duck(self):
        print(f"Утка с именем {self.name} имеет вес {self.weight}")

    def __repr__(self):
        return f"Утка {id(self)} с именем {self.name} имеет вес {self.weight}"

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


duck1 = Duck("Donald", 7)
duck2 = Duck("Dayzy", 4)

duck1.print_crack()
duck2.print_color()

duck1.print_duck()
print(str(duck2))

print(f"Больше? {duck1 > duck2}  Меньше? {duck1 < duck2}  Равно? {duck1 == duck2}  Не равно? {duck1 != duck2}")

d = duck1 + duck2
print(f"Суммарный вес: {d.weight}")

