import time
from random import randint


class Man:
    def __init__(self, name):
        self.name = name

    @staticmethod
    def solve_task():
        print("I'm not ready yet")


class Pupil(Man):
    def solve_task(self):
        sleep_time = randint(3, 6)
        time.sleep(sleep_time)
        super().solve_task()
        print(f"{self.name} has solved the task after {sleep_time} seconds")


person = Man("John")
Man.solve_task()

pupil = Pupil("John")
pupil.solve_task()
