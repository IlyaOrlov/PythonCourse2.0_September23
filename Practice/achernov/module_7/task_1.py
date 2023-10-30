class Panzer:
    def __init__(self, color, power, country, damage, name, hp):
        self.color = color
        self.power = power
        self.country = country
        self.damage = damage
        self.name = name
        self.hp = hp

    def info(self):
        print(f"Танк называется {self.name} и сделан в {self.country}. Выдерживает урон в размере {self.hp} и в ответ "
              f"наносит {self.damage}, набирает скорость в размере {self.power} км/ч")


t1 = Panzer("green", 20, "ru", 55, "T34", 220)
t2 = Panzer("grey", 30, "usa", 20, "e90", 250)
t3 = Panzer("orange", 25, "china", 20, "type", 230)

t1.info()
t2.info()
t3.info()
