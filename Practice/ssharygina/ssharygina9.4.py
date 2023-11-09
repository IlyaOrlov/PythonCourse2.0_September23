import random
import pickle


class Human:
    def __init__(self, name, surname, old, height, weight):
        self.name = name
        self.surname = surname
        self.old = old
        self.height = height
        self.weight = weight

    def __repr__(self):
        return f"[{self.name} {self.surname}, возраст: {self.old} лет, рост: {self.height} см, вес: {self.weight} кг]"


def new_human(kol):
    peoples = []
    for _ in range(kol):
        name = random.choice(["Иван", "Петр", "Аристарх", "Глеб", "Александр"])
        surname = random.choice(["Иванов", "Петров", "Сидоров", "Тапкин", "Шапкин"])
        old = random.randint(20, 45)
        height = random.randint(160, 190)
        weight = random.randint(75, 110)
        people = Human(name, surname, old, height, weight)
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


x = int(input("Введите число (сколько нужно создать экземпляров людей?): "))
p = new_human(x)
print(p)
serialize(p)
print("====================================================")
deserialize()
