class Tanks:
    def __init__(self, name, kind, damage, hp):
        self.name = name
        self.kind = kind
        self.damage = damage
        self.hp = hp

    def info(self):
        print(f"Информация о танке: название техники - {self.name}, "
              f"вид - {self.kind}, урон снарядом - {self.damage}, прочность - {self.hp}.")


t1 = Tanks("WZ-132A", "heavy", 390, 1600)
t2 = Tanks("T49", "light", 250, 1250)
t3 = Tanks("AMX", "medium", 300, 1320)
t1.info()
t2.info()
t3.info()
