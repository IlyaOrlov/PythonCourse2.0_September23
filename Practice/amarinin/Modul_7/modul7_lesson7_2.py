from time import sleep
from random import randint


class Man:

    def __init__(self, name):
        self.name = name

    def solve_task(self):
        print("I`m not ready yet")


class Pupil(Man):

    def solve_task(self):
        print("0", end="->")
        for i in range(randint(3, 6)):
            sleep(1)
            print(f"{i + 1}", end="->")
        super().solve_task()


if __name__ == "__main__":
    man = Man("As")
    man.solve_task()
    pup = Pupil("Oh")
    pup.solve_task()
