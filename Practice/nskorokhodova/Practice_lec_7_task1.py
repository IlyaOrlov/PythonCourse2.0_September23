class Tanki:
    game = "Tanchiki"

    def __init__(self, gamer, maps, tank):
        self.gamer = gamer
        self.maps = maps
        self.tank = tank


def shoot():
    print(f"Прицеливайся и стреляй")


def walk():
    print(f"Двигайся в этом направлении")


def choosetank():
    print(f"Выбери модель")


e = Tanki(gamer="Ivan", maps="№1", tank="green")
print(e.gamer)
print(e.maps)
print(e.tank)
