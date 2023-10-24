import time
import random


class Man:
    def __init__(self, name):
        self.name = name

    @staticmethod
    def solve_task():
        print("I'm not ready yet")


class Pupil(Man):
    @staticmethod
    def solve_task():
        thinking_time = random.randint(3, 6)
        time.sleep(thinking_time)
        super(Pupil, Pupil).solve_task()


x = Pupil("Иван")
x.solve_task()