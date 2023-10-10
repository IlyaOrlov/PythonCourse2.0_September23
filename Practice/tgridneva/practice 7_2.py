import time
from random import randint


class Man:
    def __init__(self, name):
        self.name = name


class Pupil(Man):
    def solve_task(self):
        sleep_time = randint(3, 6)
        time.sleep(sleep_time)
        print(f"{self.name} has solved the task after {sleep_time} seconds")


pupil = Pupil("John")
pupil.solve_task()
