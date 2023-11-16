import pickle
import random


class Human:
    def __init__(self, name, surname, age, residence):
        self.name = name
        self.surname = surname
        self.age = age
        self.residence = residence


def create_humans(num):
    human_list = []
    names = ['Мария', 'Василий', 'Петр', 'Владимир', 'София']
    surnames = ['Петров', 'Иванов', 'Сидорова', 'Криворучко', 'Бордо']
    residences = ['Москва', 'Челябинск', 'Саратов', 'Самара', 'Сочи']

    for _ in range(num):
        name = random.choice(names)
        surname = random.choice(surnames)
        age = random.randint(18, 65)
        residence = random.choice(residences)
        human = Human(name, surname, age, residence)
        human_list.append(human)

    with open('humans.data.txt', 'wb') as file:
        pickle.dump(human_list, file)


def load_humans():
    with open('humans.data.txt', 'rb') as file:
        saved_humans = pickle.load(file)
        for human in saved_humans:
            print(f"Имя: {human.name}, Фамилия: {human.surname}, Возраст: {human.age}, Город РМ: {human.residence}")


create_humans(2)
load_humans()