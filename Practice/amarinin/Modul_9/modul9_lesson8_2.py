def print_file(file):
    with open(file, "r", encoding="utf-8") as f:
        for line in f:
            yield line.rstrip("\n")


if __name__ == "__main__":
    a = print_file("my_f.txt")
    print(next(a))
    print(next(a))
    for i in a:
        print(i)
