from random import randint
from time import sleep


class Man:
    def __init__(self, name):
        self._name = name

    @staticmethod
    def solve_task():
        print("I'm not ready yet")


class Pupil(Man):

    @staticmethod
    def solve_task():
        sleep(randint(3, 6))
        

man1 = Man("Андрей")
man1.solve_task()
man2 = Pupil("Не Андрей")
man2.solve_task()
