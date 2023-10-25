import pickle
import random


class Human:
    def __init__(self, name, surname, age, town, education, profession):
        self.name = name
        self.surname = surname
        self.age = age
        self.town = town
        self.education = education
        self.profession = profession

    def info(self):
        print(f"Кандидата зовут {self.name} {self.surname}, ей {self.age} лет. Живет в городе {self.town}. "
              f"Имеет {self.education} образование по профессии: {self.profession}." )


def create(x):
    humans = []
    for i in range(x):
        name = random.choice(["Татьяна", "Ирина", "Полина", "Кира"])
        surname = random.choice(["Петрова", "Львова", "Точкина", "Швецова"])
        age = random.randint(18, 70)
        town = random.choice(["Нижний Новгород", "Москва", "Киров", "Владимир"])
        education = random.choice(["высшее - бакалавриат", "среднее профессиональное",
                                           "высшее - специалитет", "высшее - магистратура"])
        profession = random.choice(["экономист", "программист", "инженер-технолог", "повар"])
        h = Human(name, surname, age, town, education, profession)
        humans.append(h)
    return humans

def ser(humans):
    with open("human.data", "wb") as f:
        pickle.dump(humans, f)

def des():
    with open("human.data", "rb") as f:
        h = pickle.load(f)
        print(h)


hum = create(3)
for i in hum:
    i.info()
ser(hum)
des()
