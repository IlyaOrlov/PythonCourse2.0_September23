start = input("Топлива было: ")
end = input("Топлива осталось: ")
distance = input("Расстояние: ")

diff = int(start) - int(end)
result = diff / int(distance)

# на всякий случай исправил:)
print(f"Средний расход бензина: {result} (литров на 1 км)")
