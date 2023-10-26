class Tanki:
    game = "Tanchiki"

    def __init__(self, nikname, country, age, tank):
        self.nikname = nikname
        self.country = country
        self.age = age
        self.tank = tank


e = Tanki(nikname="Ivan", country="Russia", age=30, tank=5)
e1 = Tanki(nikname="Ricardo", country="Portugal", age=17, tank=3345)
print(e.nikname, e.country, e.age, e.tank)
print(e1.nikname, e1.country, e1.age, e1.tank)
