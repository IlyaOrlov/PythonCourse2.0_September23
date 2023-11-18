import random
import pickle


class Human:
    def __init__(self):
        self.gender = random.choice(["Man", "Woman"])
        self.age = random.randint(18, 56)
        self.weight = random.randint(45, 90)
        self.height = random.randint(100, 150)


def pic_send(n):
    lst_inf_human = [i.__dict__ for i in [Human() for _ in [str(i + 1) for i in range(n)]]]
    with open('human.data', "wb") as f:
        pickle.dump(lst_inf_human, f)


def pic_reception(file):
    with open(file, "rb") as f:
        lst_inf_human = pickle.load(f)
    for i in lst_inf_human:
        print(i)


if __name__ == "__main__":

    pic_send(5)
    pic_reception('human.data')
