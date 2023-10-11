from time import sleep
from random import randint


class Man:
    def __init__(self, name):
        self._name = name

    @staticmethod
    def solve_task():
        print("I'm not ready yet.")


class Pupil(Man):

    def solve_task(self):
        sleep(randint(3, 6))
        super().solve_task()


m1 = Man("Aleksandr")
m1.solve_task()
p1 = Pupil("Klim")
p1.solve_task()
