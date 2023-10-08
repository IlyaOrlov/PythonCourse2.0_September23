class Duck:
    color = "yellow"

    def __init__(self, name, weight):
        self.name = name
        self.weight = weight

    @staticmethod
    def quack():
        print("Quack")

    @classmethod
    def get_color(cls):
        print(f"The color of ducks is {cls.color}")

    def display_info(self):
        print(f"Name: {self.name}, Weight: {self.weight}")

    def __repr__(self):
        return f"Duck(name={self.name}, weight={self.weight})"

    def __lt__(self, other):
        return self.weight < other.weight

    def __gt__(self, other):
        return self.weight > other.weight

    def __eq__(self, other):
        return self.weight == other.weight

    def __ne__(self, other):
        return self.weight != other.weight

    def __add__(self, other):
        total_weight = self.weight + other.weight
        return Duck("Combined Duck", total_weight)


duck1 = Duck("Donald", 10)
duck2 = Duck("Daisy", 8)
duck1.quack()
Duck.get_color()
duck1.display_info()
duck2.display_info()

print(duck1)
print(duck1 < duck2)
print(duck1 > duck2)
print(duck1 == duck2)
print(duck1 != duck2)

combined_duck = duck1 + duck2
print(combined_duck)
