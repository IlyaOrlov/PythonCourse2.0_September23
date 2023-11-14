from time import sleep
from random import randint


class Man:
    def __init__(self, name):
        self._name = name

    @staticmethod
    def solve_task():
        print("I'm not ready yet.")


class Pupil(Man):

    @staticmethod
    def solve_task():
        sleep(randint(3, 6))
        super(Pupil, Pupil).solve_task()


m1 = Man("Maksimilian")
m1.solve_task()
p1 = Pupil("Reer")
p1.solve_task()
