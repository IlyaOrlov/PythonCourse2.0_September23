def read_str(file):
    with open(file, "r", encoding="utf-8") as f:
        for line in f:
            yield line


file1 = input("Введите имя файла: ")
for x in read_str(file1):
    print(x)
