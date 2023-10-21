class Tank:
    id = ""
    model = "Т-72"
    weight = 46
    gun_mm = 125
    point = 0

    def __init__(self, id):
        self.id = id

    def go(self, point):
        self.point = self.point + point
        print(f"Танк {self.id} проехал {point} метров")
    def shoot (self):
        print(f"Танк {self.id} сделал выстрел!")

t1 = Tank(1)
t2 = Tank(2)

t1.go(20)
t1.shoot()
t2.go(50)
t1.go(10)
t2.shoot()
t2.go(33)
print(f"Координаты танков: {t1.point=} и {t2.point=}")
