def gen_read(file):
    with open(file, "r", encoding="utf-8") as f:
        for line in f:
            yield line


if __name__ == "__main__":
    my_file = input("Введите имя файла: ")
    for x in gen_read(my_file):
        print(x)
