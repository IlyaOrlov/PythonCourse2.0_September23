class Tank:
    def __init__(self, name, weight, power, color):
        self.name = name
        self.weight = weight
        self.power = power
        self.color = color

    def info(self):
        print(f"Название танка - {self.name}, "
              f"вес - {self.weight}, сила удара - {self.power}, цвет - {self.color}.")


t1 = Tank("Первый", "100", 1, "белый")
t2 = Tank("Второй", "200", 2, "черный")
t3 = Tank("Третий", "300", 3, "голубой")
t1.info()
t2.info()
t3.info()