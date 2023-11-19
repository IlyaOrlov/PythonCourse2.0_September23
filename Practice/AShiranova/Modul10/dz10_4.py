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
        name = random.choice(["Андрей", "Илья", "Максимилиан", "Егор", "Сергей", "Матвей"])
        surname = random.choice(["Ширанов", "Иванов", "Глынин", "Тельминов", "Смирнов", "Егоров"])
        old = random.randint(1, 99)
        residence = random.choice(["Москва", "Ижевск", "Нижний Новгород", "Омск", "Бор", "Сочи"])
        height = random.randint(50, 200)
        weight = random.randint(3, 200)
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


A = int(input("Количество экземпляров: "))
B = fact_human(A)
print(B)
serialize(B)
deserialize()
