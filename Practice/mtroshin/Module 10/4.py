# Создать класс Human с 5-10 атрибутами (имя, фамилия, возраст, меcто жительства и т.д.).
# Написать функцию, которая создавала бы указанное количество экземпляров, сериализовывала
# их и сохраняла в файл human.data, и другую функцию, которая бы читала файл human.data,
# десериализовывала его содержимое и выводила результат на печать. Примечание: чтоб у экземпляров
# Human были разные значения атрибутов, можно воспользоваться функциями random.randint() и random.choice().

import random
import pickle

class Human:
    def __init__(self, name, surname, age, city, country):
        self.name = name
        self.surname = surname
        self.age = age
        self.city = city
        self.country = country

    def print_info(self):
        print(f"Name: {self.name}, Surname: {self.surname}, Age: {self.age}, City: {self.city}, Country: {self.country}")


def create_and_save_humans(humans_count):
        humans = []
        for i in range(humans_count):
            name = random.choice(['Диана', 'Даша', 'Миша', 'Женя', 'Марина'])
            surname = 'Трошин(а)'
            age = random.randint(1, 60)
            city = random.choice(['Питер','Орел'])
            country = 'Россия'
            human = Human(name,surname,age,city,country)
            humans.append(human)

        with open('Humans_dump.pkl', "wb") as file:
            for human in humans:
                print(human.name, human.surname, human.age, human.city, human.country)
                pickle.dump((human.name, human.surname, human.age, human.city, human.country), file)

def load_print_dump(counts):
    i=1
    with open('Humans_dump.pkl','rb') as file:
        while i < counts:
            content = pickle.load(file)
            print(content)
            i+=1

create_and_save_humans(5)
load_print_dump(5)