class Tank:
    def __init__(self, name, country, price, speed, weight, armor, damage):
        self.name = name
        self.country = country
        self.price = price
        self.speed = speed
        self.weight = weight
        self.armor = armor
        self.damage = damage

    def characteristics(self):
        print(f"Название: {self.name}\nCтрана: {self.country}\n"
              f"Цена: {self.price}\nСкорость: {self.speed}\n"
              f"Вес: {self.weight}\nБроня: {self.armor}\nУрон : {self.damage}\n")


t1 = Tank("Pobeda", "Russia", 30000, 40, 200, 20, 100)
t2 = Tank("Kosmos", "USA", 10000, 30, 180, 15, 70)
t1.characteristics()
t2.characteristics()

