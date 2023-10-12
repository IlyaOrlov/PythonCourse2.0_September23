from abc import ABC, abstractmethod

class Pizza(ABC):
    @staticmethod
    def prepare():
        print("Готовим тесто")

    @staticmethod
    @abstractmethod
    def add_ingr():
        pass

    @staticmethod
    def bake():
        print("Греем пиццу...")
        print("Готово")


class VegPizza(Pizza):
    @staticmethod
    def add_ingr():
        print("Добавляем овощи")


class MeatPizza(Pizza):
    @staticmethod
    def add_ingr():
        print("Добавляем мясо")


class MushPizza(Pizza):
    @staticmethod
    def add_ingr():
        print("Добавляем грибы")


class CheezePizza(Pizza):
    @staticmethod
    def add_ingr():
        print("Добавляем сыр")


def make_pizza(p):
    p.prepare()
    p.add_ingr()
    p.bake()


pizza_types = (VegPizza, MeatPizza, MushPizza, CheezePizza)

# lst = []
# for i, pc in enumerate(pizza_types):
#     lst.append((i, pc.__name__))

pizza_dict = {i: pc.__name__ for i, pc in enumerate(pizza_types)}
p = input(f"Выберите пиццу: {pizza_dict}: ")

if p.isdecimal() and 0 <= (n := int(p)) < len(pizza_types):
    pizza = pizza_types[n]()
    if isinstance(pizza, Pizza):
        print(f"Yes: {type(pizza)}")

    make_pizza(pizza)
else:
    pizza = None


