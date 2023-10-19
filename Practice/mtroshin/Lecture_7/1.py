class tank:
    id = ""
    model = "Т-72"
    massa = 46
    pushka_mm = 125
    dvigatel = 1130
    boekomplekt = 41

    def __init__(self, id):
        self.id = id

t = tank(1)
t2 = tank(2)
