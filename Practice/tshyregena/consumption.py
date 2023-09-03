start = input("Топлива было: ")  # Надо ли указывать единицы измерения?
end = input("Топлива осталось: ")
distance = input("Расстояние: ")
diff = int(start) - int(end)
result = diff / int(distance)
print(f"Расход бензина: {result} ")
