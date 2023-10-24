import pickle
import random


class Human:
    def __init__(self, name, surname, old, residence, height, weight):
        self.name = name
        self.surname = surname
        self.old = old
        self.residence = residence
        self.height = height
        self.weight = weight

    def __repr__(self):
        return (f"[{self.name} {self.surname}, возраст {self.old},"
                f" рост {self.height}, вес {self.weight}]")


def fact_human(kol):
    peoples = []
    for _ in range(kol):
        name = random.choice(["Ivan", "Alex", "Sergey", "Vasiliy", "Kosmos"])
        surname = random.choice(["Ivanov", "Petrov", "Sidorov", "Rogov", "Vasiliev"])
        old = random.randint(18, 55)
        residence = random.choice(["London", "Paris", "New York", "Moscow", "Nizhny Novgorod"])
        height = random.randint(160, 210)
        weight = random.randint(40, 150)
        people = Human(name, surname, old, residence, height, weight)
        peoples.append(people)
    return peoples


def serialize(peoples):
    with open("human.data", "wb") as file:
        pickle.dump(peoples, file)


def deserialize():
    with open("human.data", "rb") as file:
        peoples = pickle.load(file)
        for people in peoples:
            print(people)


k = int(input("Введите количество людей: "))
p = fact_human(k)
print(p)
serialize(p)
deserialize()
