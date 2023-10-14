class Tank:
    def __init__(self, number, color, speed, accuracy, state="Живой"):
        self.number = number
        self.color = color
        self.speed = speed
        self.accuracy = accuracy
        self.state = state


class Building:
    def __init__(self, length, width, coordinate=None):
        self.length = length
        self.width = width
        self.coordinate = coordinate


class Field:
    def __init__(self, length, width, building=None):
        self.length = length
        self.width = width
        self.building = building


tank1 = Tank(1, "red", 20, 70)
tank2 = Tank(2, "blue", 15, 85)
build1 = Building(15, 5, (15, 20))
build2 = Building(5, 3, (85, 70))
field = Field(100, 50, {build1, build2})

print(f"На поле с размерами [{field.length},{field.width}] количество строений: {len(field.building)} ")
print(f"Сражаются танки: {tank1.color} со скоростью {tank1.speed} и вероятностью попадания {tank1.accuracy}% и "
      f"{tank2.color} со скоростью {tank2.speed} и вероятностью попадания {tank2.accuracy}%")

