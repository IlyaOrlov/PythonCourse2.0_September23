
def gen(name):
    with open(name, "r", encoding="utf-8") as file:
        for line in file:
            print(file.readline())
            yield line


r = input("Введите имя файла: ")
for i in gen(r):
    print(i)
# print(next(r))
# print(next(r))
# print(next(r))
