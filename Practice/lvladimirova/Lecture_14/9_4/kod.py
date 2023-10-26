import random


class Human:
    def __init__(self, name, surname, age, city, work):
        self._name = name
        self._surname = surname
        self._age = age
        self._city = city
        self._work = work

    def print_name(self):
        print(f"Перед вами {self._name} {self._surname}. Ему {self._age} лет. Живёт в городе {self._city}."
              f" Работает в компании {self._work}")


def create_instances(num):
    people = []
    for i in range(num):
        name = random.choice(["Иван", "Пётр", "Дмитрий"])
        surname = random.choice(["Иванов", "Петров", "Сидоров"])
        age = random.randint(20, 60)
        city = random.choice(["Нижний Новгород", "Москва", "Владивосток"])
        work = random.choice(["ООО Альфа", "ОАО Бета", "ЗАО Гамма"])
        i = Human(name, surname, age, city, work)
        people.append(i)
    return people
