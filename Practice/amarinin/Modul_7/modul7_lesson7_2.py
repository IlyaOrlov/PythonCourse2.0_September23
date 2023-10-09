from time import sleep
from random import randint


class Man:

    def __init__(self, name):
        self.name = name

    @staticmethod
    def solve_task():
        print("I`m not ready yet")


class Pupil(Man):

    @staticmethod
    def solve_task():
        print("0", end="")
        for i in range(randint(3, 6)):
            sleep(1)
            print(f"_{i + 1}", end="")
        print("\nI`m not ready yet")


if __name__ == "__main__":
    man = Man("As")
    man.solve_task()
    pup = Pupil("Oh")
    pup.solve_task()
