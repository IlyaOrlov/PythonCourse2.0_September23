import time
import random


class Man:
    def __init__(self, name):
        self._name = name

    def solve_task(self):
        print("I'm not ready yet")


class Pupil(Man):
    def solve_task(self):
        super().solve_task()
        time.sleep(random.randint(3, 6))


per1 = Pupil("Артем")
per2 = Man("Григорий")
per1.solve_task()
per2.solve_task()
