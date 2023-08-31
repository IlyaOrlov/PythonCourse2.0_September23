start = input("Топлива было: ")
end = input("Топлива осталось: ")
diff = int(start) - int(end)
distance = input("Расстояние: ")
result = diff / int(distance)
print(f"Расход бензина: {result}")

