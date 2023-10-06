class Duck:
    color = "Red"

    def __init__(self, name, weight):
        self.name = name
        self.weight = weight
        print(f"Ура! Я новая Уточка! Меня зовут {self.name}.")

    @staticmethod
    def voice():
        print("Crack")

    @classmethod
    def duck_color(cls):
        print(f"Color    : {cls.color}")

    def duck_name(self):
        print(f"Name     : {self.name}")

    def duck_weight(self):
        print(f"Weight   : {self.weight}")

    def __add__(self, other):
        super_duck = Duck("КАДАВР", self.weight + other.weight)
        print(f"Я пожиратель уток, мой вес  {self.weight + other.weight} кг.")
        return super_duck

    def __lt__(self, other):
        return True if self.weight < other.weight else False

    def __eq__(self, other):
        return True if self.weight == other.weight else False

    def __ne__(self, other):
        return True if self.weight != other.weight else False

    def __str__(self):
        return f"\nУтка\nкласс:{type(self).__name__}\nимя  :{self.name}\nвес  :{self.weight}\nцвет :{Duck.color}"

    def __repr__(self):
        return f"Класс {type(self).__name__} {self.name=} {self.weight=} {Duck.color=}"


if __name__ == "__main__":
    duck1 = Duck("Dudu", 100)
    duck2 = Duck("Zuzu", 50)
    duck1.duck_name()
    super_duck = duck1 + duck2 + duck2
    super_duck = super_duck + super_duck
    super_duck.duck_weight()
    super_duck.voice()
    print(duck1 > duck2)
    a = super_duck == duck1
    print(a)
    print(duck1)
    print(repr(duck2))
