import random
import json


class Human:
    def __init__(self, name, surname, age, residence):
        self.name = name
        self.surname = surname
        self.age = age
        self.residence = residence


def generate_humans(count):
    attributes = [
        {"name": "John", "surname": "Doe", "age": 25, "residence": "New York"},
        {"name": "Jane", "surname": "Smith", "age": 30, "residence": "London"},
        {"name": "Mike", "surname": "Johnson", "age": 35, "residence": "Paris"},
        {"name": "Anna", "surname": "Davis", "age": 28, "residence": "Berlin"},
        {"name": "Alex", "surname": "Wilson", "age": 32, "residence": "Tokyo"}
    ]
    humans = []
    for _ in range(count):
        attributes_dict = random.choice(attributes)
        human = Human(attributes_dict["name"], attributes_dict["surname"], attributes_dict["age"],
                      attributes_dict["residence"])
        humans.append(human)
    return humans


def serialize_humans(humans):
    serialized_humans = []
    for human in humans:
        serialized_human = {
            "name": human.name,
            "surname": human.surname,
            "age": human.age,
            "residence": human.residence
        }
        serialized_humans.append(serialized_human)

    with open("human.data", "w") as file:
        json.dump(serialized_humans, file)


def deserialize_humans():
    with open("human.data", "r") as file:
        serialized_humans = json.load(file)

    humans = []
    for serialized_human in serialized_humans:
        human = Human(serialized_human["name"], serialized_human["surname"], serialized_human["age"],
                      serialized_human["residence"])
        humans.append(human)
    return humans


# Создаем и сериализуем экземпляры Human
humans_to_serialize = generate_humans(5)
serialize_humans(humans_to_serialize)

# Десериализуем экземпляры Human и выводим результат на печать
deserialized_humans = deserialize_humans()
for human in deserialized_humans:
    print(f"Name: {human.name}")
    print(f"Surname: {human.surname}")
    print(f"Age: {human.age}")
    print(f"Residence: {human.residence}")
    print("---------------------")
