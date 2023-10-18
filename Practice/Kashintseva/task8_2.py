def reading(file):
    with open(file, "r", encoding="utf-8") as f:
        s = f.readlines()
        for r in s:
            yield r.strip()


file = input("Введите путь к файлу: ")
for n in reading(file):
    print(n)
