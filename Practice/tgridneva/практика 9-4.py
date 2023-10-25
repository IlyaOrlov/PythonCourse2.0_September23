import random
import pickle


class Human:
    def __init__(self, name, surname, age, residence):
        self.name = name
        self.surname = surname
        self.age = age
        self.residence = residence

    def __str__(self):
        return f"Имя: {self.name}\nФамилия: {self.surname}\nВозраст: {self.age}\nМесто жительства: {self.residence}"


def create_humans(num_humans):
    humans = []
    for _ in range(num_humans):
        name = random.choice(["Иван", "Игорь", "Михаил", "Дмитрий"])
        surname = random.choice(["Иванов", "Смирнов", "Сидоров", "Волков"])
        age = random.randint(18, 60)
        residence = random.choice(["Нижний Новгород", "Москва", "Санкт Петербург", "Калининград"])
        human = Human(name, surname, age, residence)
        humans.append(human)
    return humans


def serialize_humans(humans):
    with open("human.data", "wb") as file:
        pickle.dump(humans, file)


def deserialize_humans():
    with open("human.data", "rb") as file:
        humans = pickle.load(file)
    return humans


humans = create_humans(5)

serialize_humans(humans)

deserialized_humans = deserialize_humans()
for human in deserialized_humans:
    print(human)
    print()
