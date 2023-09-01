import math


def square(r):
    return math.pi * r ** 2


if __name__ == "__main__":
    radius = float(input("Введите радиус: "))
    result = square(radius)
    print(f"\nПлощадь круга : {round(result, 2)}")
