import pickle
import random


class Human:
    def __init__(self, name, surname, old, salary, city):
        self.name = name
        self.surname = surname
        self.old = old
        self.salary = salary
        self.city = city
        

def create_hum(kol):
    peoples = []
    for _ in range(kol):
        name = random.choice(["Андрей", "Пётр", "Витя", "Ильяс", "Ренат"])
        surname = random.choice(["Андреев", "Петров", "Викторов", "Ильясов", "Ренатов"])
        old = random.randint(20, 35)
        salary = random.randint(10000, 20000)
        city = random.choice(["NN", "MSK", "SPB", "KZN", "UFA"])
        new_people = Human(name, surname, old, salary, city)
        peoples.append(new_people)
    return peoples


def serialize(peoples):
    with open("human.data", "wb") as file:
        pickle.dump(peoples, file)


def deserialize():
    with open("human.data", "rb") as file:
        peoples = pickle.load(file)
        for people in peoples:
            print(people)


k = int(input("Введите число"))
p = create_hum(k)
print(p)
serialize(p)
deserialize()
