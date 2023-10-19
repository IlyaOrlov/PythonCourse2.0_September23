import os


def read(f):
    with open(f, "r", encoding="utf-8") as file1:
        for line in file1:
            line = line.rstrip("\n")
            yield line


def delete(f):
    os.remove(f)


with open("f.txt", "w", encoding="utf-8") as file:
    file.write("Пример1\nПример2\nПример3\n")

for line1 in read("f.txt"):
    print(line1)

delete("f.txt")
