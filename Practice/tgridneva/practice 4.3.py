while (x := input())[:1].lower() + x[1:] != 'stop':
    print(x)
while True:
    user_input = input("Введите число: (или 'stop' для выхода): ")
    if user_input == "stop":
        break
    print("Вы ввели:", user_input)

print("Выход")
