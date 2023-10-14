class Panzer:

    def __init__(self, names, types, nation, weight, forward, backward):
        self.names = names
        self.types = types
        self.nation = nation
        self.weight = weight
        self.forward = forward
        self.backward = backward

    def info(self):
        print(f"\nClass  : {type(self).__name__}")
        print(f"Name   : {self.names}")
        print(f"Type   : {self.types}")
        print(f"Nation : {self.nation}")
        print(f"Weight : {self.weight}")
        print(f"Forward  : {self.forward}")
        print(f"Backward : {self.backward}")


if __name__ == "__main__":
    t1 = Panzer("T-34", "Light", "USSR", 30, 48, 18)
    print(t1.backward)
    t1.info()
    t2 = Panzer("Tiger II", "Heavy", "GERMANY", 71, 35, 12)
    t2.info()
