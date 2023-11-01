class Tank:
    def __init__(self, name, speed, v):
        self.name = name
        self.speed = speed
        self.v = v

    def sv(self):
        print(f"Название: {self.name}.\nСкорость: {self.speed} км/ч.\nВыстрел: {self.v}\n")


t1 = Tank("Танк А", 180, "Бум!")
t2 = Tank("Танк В", 200, "Бабах!")
t1.sv()
t2.sv()
