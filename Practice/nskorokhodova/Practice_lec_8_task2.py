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
        time.sleep(random.randint(3, 6))
        super(Pupil, Pupil).solve_task()


man1 = Pupil("Igor")
man1.solve_task()
man2 = Pupil("Anatolii")
man2.solve_task()
