time = float(input("Введите потраченное время (мин): "))
distance = float(input("Введите расстояние (км): "))
speed = distance / (time / 60)
print(f"Средняя скорость во время поездки: {round(speed, 1)} км/ч")
