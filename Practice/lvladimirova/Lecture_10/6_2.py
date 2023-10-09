class Duck:
    color = "серый"

    def __init__(self, name, weight):
        print("\nПривет! Новая уточка с вами!")
        self.name = name
        self.weight = weight

    @staticmethod
    def say_crack():
        print("Кряяяяяя!")

    def info_duck(self):
        print(f"Меня зовут: {self.name}, мой вес: {self.weight} кг")

    def __repr__(self):
        return f"У нас появилась уточка {self.name}, вес уточки {self.weight} кг"

    @classmethod
    def duck_color(cls):
        print(f"Цвет уточки: {cls.color}")

    def __lt__(self, other):  # меньше чем
        return self.weight < other.weight

    def __gt__(self, other):  # больше чем
        return self.weight > other.weight

    def __eq__(self, other):
        return self.weight == other.weight

    def __ne__(self, other):
        return self.weight != other.weight

    def __add__(self, other):
        new_weight = self.weight + other.weight
        super_duck = Duck(None, new_weight)
        print(f"Вес двух уточек: {self.weight + other.weight} кг.")
        return super_duck


duck1 = Duck("Дональд", 7)
duck1.say_crack()
duck1.info_duck()
duck1.duck_color()
print(duck1)

duck2 = Duck("Билли", 5)
duck2.say_crack()
duck2.info_duck()
duck2.duck_color()
print(duck2)

duck3 = Duck("Вилли", 9)
duck3.say_crack()
duck3.info_duck()
duck3.duck_color()
print(duck3)

print("===============================")
print(duck1 < duck2)
print("===============================")
print(duck2 > duck3)
print("===============================")
print(duck2 == duck3)
print("===============================")
print(duck2 != duck3)
print("===============================")
mega_duck = duck1 + duck3
print(mega_duck.weight)
