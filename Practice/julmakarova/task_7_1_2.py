import time
import random


class Man:
    def __init__(self, name):
        self._name = name

    @staticmethod
    def solve_task():
        print("I'm not ready yet")


class Pupil(Man):
    def solve_task(self):
        time.sleep(random.randint(3, 6))
        super().solve_task()


m = Man("Mihail")
m.solve_task()

p = Pupil("Valeriy")
p.solve_task()


