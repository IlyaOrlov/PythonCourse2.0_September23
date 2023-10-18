def read(f):
    with open(f, "r", encoding="utf-8") as file1:
        for line in file1:
            if "\n" in line:
                line = line[:-1]
                yield line


with open("f.txt", "w", encoding="utf-8") as file:
    file.write("Пример1\nПример2\nПример3\n")

for line1 in read("f.txt"):
    print(line1)
