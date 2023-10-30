class Duck:
    color = "Yellow"

    def __init__(self, name, weight):
        self.name = name
        self.weight = weight

    @staticmethod
    def voice():
        print("Кряк")

    @classmethod
    def pet_color(cls):
        print(f"Цвет: {cls.color}")

    def pet_name(self):
        print(f"Имя: {self.name}")

    def pet_weight(self):
        print(f"Вес: {self.weight}")

    def pet_info(self):
        print(f"Меня зовут: {self.name} и вешу я {self.weight}. Мой цвет как у всех {self.color}")

    def __repr__(self):
        return f"Утка: {self.name} и весит: {self.weight}"

    def __lt__(self, other):
        return self.weight < other.weight

    def __gt__(self, other):
        return self.weight > other.weight

    def __ne__(self, other):
        return self.weight != other.weight

    def __add__(self, other):
        new_weight = self.weight + other.weight
        new_duck = Duck(None, new_weight)
        print(f"Вес двух уток: {self.weight + other.weight}")
        return new_duck


duck_1 = Duck("Скрудж", 10)
duck_1.pet_name()
duck_1.pet_weight()
duck_1.voice()
duck_1.pet_info()

duck_2 = Duck("Зигзаг", 15)
duck_2.pet_name()
duck_2.pet_weight()
duck_2.voice()
duck_2.pet_info()

print("Работа __repr__")
print(repr(duck_1))
print("Работа __lt__")
print(duck_1 < duck_2)
print("Работа __gt__")
print(duck_1 > duck_2)
print("Работа __ne__")
print(duck_1 != duck_2)
duck_3 = duck_1 + duck_2
print(duck_3.weight)
