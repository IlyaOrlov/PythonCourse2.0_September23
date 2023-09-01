if __name__ == "__main__":
    length = float(input("Введите длину пути (км)  : "))
    time = float(input("Введите время в пути (ч) : "))
    speed = length / time
    print(f"\nСредняя скорость равна  {round(speed, 1)}  км. в час")
