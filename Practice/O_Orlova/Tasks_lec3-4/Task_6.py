start = input("Топлива было: ")               # без точек с запятой каждое условие с новой строки
end = input("Топлива осталось: ")
distance = input("Расстояние: ")
diff = int(start) - int(end)
result = diff / int(distance)         # явно указываем интерпретатору, что надо делить на число
print(f"Расход бензина: {result}")
