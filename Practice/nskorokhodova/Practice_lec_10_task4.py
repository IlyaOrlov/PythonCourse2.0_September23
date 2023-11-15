import pickle
import random


class Human:
    def __init__(self, name, surname, age, address):
        self.name = name
        self.surname = surname
        self.age = age
        self.address = address


def create_humans(num_humans):
    humans = []
    for _ in range(num_humans):
        name = random.choice(["Иван", "Мария", "Михаил", "Александр", "Алла"])
        surname = random.choice(["Иванов", "Олешко", "Смирнов", "Моисеев", "Копытова"])
        age = random.randint(18, 65)
        address = random.choice(["Москва", "Лондон", "Нижний Новгород", "Пермь", "Омск"])
        human = Human(name, surname, age, address)
        humans.append(human)
    return humans


def serialize(humans):
    with open("human.data", "wb") as file:
        pickle.dump(humans, file)


def deserialize():
    with open("human.data", "rb") as file:
        humans = pickle.load(file)
        for human in humans:
            print(human.name, human.surname, human.age, human.address)


x = int(input("Введите число "))
p = create_humans(x)
serialize(p)
deserialize()
