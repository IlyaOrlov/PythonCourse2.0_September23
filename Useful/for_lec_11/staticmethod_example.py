import random


class Employee:
    def __init__(self):
        self.name = self.generate_name()

    @staticmethod
    def generate_name():
        s = ""
        for _ in range(5):
            s += random.choice("абеюуиколын")
        return s


e = Employee()
print(e.name)