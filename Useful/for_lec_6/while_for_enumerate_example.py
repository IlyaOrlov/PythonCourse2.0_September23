# Найти цифровой символ в строке
s = "aqnrnn9mtm"

# Способ 1:
i = 0
while i < len(s):
    if s[i].isdecimal():
        print(f"Нашли: индекс = {i}, значение = {s[i]}")
        break
    i += 1
else:
    print("Цифровой символ не найден")

# Способ 2:
i = 0
for x in s:
    if x.isdecimal():
        print(f"Нашли: индекс = {i}, значение = {s[i]}")
        break
    i += 1
else:
    print("Цифровой символ не найден")

# Способ 3 (лучший, если нужен индекс):
for i, x in enumerate(s):
    if x.isdecimal():
        print(f"Нашли: индекс = {i}, значение = {s[i]}")
        break
else:
    print("Цифровой символ не найден")
