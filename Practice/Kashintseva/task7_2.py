import time
import random


class Man:
    def __init__(self, name):
        self._name = name

    def solve_task(self):
        print("I'm not ready yet")


class Pupil(Man):
    def __init__(self, name):
        super().__init__(name)

    def solve_task(self):
        time.sleep(random.randint(3, 6))
        print("I'm ready")


per1 = Pupil("Артем")
per2 = Man("Григорий")
per1.solve_task()
per2.solve_task()
