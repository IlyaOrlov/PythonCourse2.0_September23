# Задание 2. Класс Duck.
class Duck:
    color = "Зеленый"
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight
        print(f"Утка {self.name}.")

    @staticmethod
    def print_crack():
        print("Crack")

    @classmethod
    def print_color(cls, new_cvet):
        cls.cvet = new_cvet
        print(cls.cvet)

    def print_name_weight(self):
        print(f"{self.name}, {self.weight}")

    def __lt__(self, other):
        if self.name == other.name:
            return self.weight < other.weight
        else:
            return self.name < other.name

    def __repr__(self):
        return f"Duck at {id(self)}:{self.name}, {self.weight}, {self.cvet}"

    def __str__(self):
        return f"Duck:{self.name}, {self.weight}, {self.cvet}"


    def __add__(self, other):
        sum_weight = self.weight + other.weight
        new_duck = Duck(None, sum_weight)
        return new_duck

    def __gt__(self, other):
        if self.name == other.name:
            return self.weight > other.weight
        else:
            return self.name > other.name


    def __eq__(self, other):
        return self.weight == other.weight

    def __ne__(self, other):
        return self.weight != other.weight

class Duckling():
    pass


w = Duck("Утенок", 5)
w.print_crack()
w.print_color("Серый")
print(w.cvet)
w.print_name_weight()
print(w)
print(repr(w))

d1 = Duck("Кря", 50)
d2 = Duck("Ряк", 100)
d3 = Duck("Кря", 100)
d4 = Duck("Ркя", 90)

s = d3 + d4
print(f"Общий вес уток = {s.weight}")
print(d2 > d4)
print(d2 < d4)
print(d2 == d4)
print(d2 != d4)
# Попробовал сортировку с < и > по отдельности все работает.
# При наличии двух магических методов < и >, используется первый в записи.
# Для равно и неравно естественно сортировка не работает.
spisok = [d1, d2, d3, d4]
for i in spisok:
    print(i)
print("**********************")
spisok.sort()
for i in spisok:
    print(i)
