def reading(fil):
    with open(file, "r", encoding="utf-8") as f:
        for line in f:
            yield line


file = input("Введите путь к файлу: ")
for n in reading(file):
    print(n)
