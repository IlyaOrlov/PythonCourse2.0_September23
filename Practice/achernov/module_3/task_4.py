string = input("Введите строку: ")
print(f"Изначальная строка: {string}")
change_symbol = ["A", "А"]
for symbol in change_symbol:
    string = string.replace(symbol, "*")
print(f"Новая строка: {string}")
