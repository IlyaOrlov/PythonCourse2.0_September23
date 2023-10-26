import random
import pickle


class Human:
    def __init__(self, name, surname, age, address, child):
        self.name = name
        self.surname = surname
        self.age = age
        self.address = address
        self.child = child

    def __str__(self):
        return (f"{self.surname} {self.name} {self.age} age, address {self.address} have {self.child} child")


def in_file(num_human):
    name = ("Ivan", "Pavel", "Petr", "Sergey", "Anton")
    surname = ("Ivanov", "Petrov", "Morozov", "Sergeev", "Sokolov")
    address = ("Surikova 5", "Gagarina 132", "Svobody 2", "Belinsky 56", "Beketova 8")

    lst_hum = []
    for i in range(num_human):
        hum = Human(random.choice(name), random.choice(surname), random.randint(20, 50), random.choice(address),
                    random.randint(0, 5))
        print(hum)
        lst_hum.append(hum)

    with open('human.data.txt', "wb") as f:
        pickle.dump(lst_hum, f)


def out_file(name_file):
    with open(name_file, "rb") as f:
        data = pickle.load(f)

    for hum in data:
        print(hum)


in_file(6)
print("=============")
out_file('human.data.txt')
