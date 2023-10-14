class Tank:
    def __init__(self, name, health):
        self.name = name
        self.health = health

    def shoot(self):
        print(f"{self.name} совершает выстрел!")


tank1 = Tank("Танк 1", 100)
tank2 = Tank("Танк 2", 150)
tank1.shoot()
tank2.shoot()
