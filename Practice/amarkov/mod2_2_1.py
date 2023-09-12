import math


def square(r):
    return math.pi * r ** 2


if __name__ == "__main__":
    radius = input("Введите радиус: ")
    result = square(int(radius))
    print(f"Площадь круга: {result}")