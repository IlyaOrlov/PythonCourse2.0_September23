start = input("Топлива было: ")  # оставлять несколько инструкций на одной строке не рекомендуется
end = input("Топлива осталось: ")
distance = input("Расстояние: ")
diff = int(start) - int(end)
result = diff / int(distance)  # переменную distance нужно было преобразовать в число
print(f"Расход бензина: {result}")
