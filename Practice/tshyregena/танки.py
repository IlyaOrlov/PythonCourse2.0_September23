class Tanks:
    def __init__(self, name, color, armor, speed, power):
        self.name = name
        self.color = color
        self.armor = armor
        self.speed = speed
        self.power = power

    def print_p(self):
        print(
            f"Я персонаж {id(self)}: {self.name=}, мой цвет {self.color=}. Моя броня {self.armor=}\n и я двигаюсь я со скоростью {self.speed=}. Моя сила {self.power=}")


p1 = Tanks('Рыжик', "синий", '50', "4", 100)
p1.print_p()  # Employee.print_emp(e1)
p2 = Tanks('Лина', 'розовый', '60', '150', '500')
p2.print_p()
