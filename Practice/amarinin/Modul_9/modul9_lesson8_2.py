def print_file(file):
    res = ""
    with open(file, "r", encoding="utf-8") as f:
        for char in f.read():
            if char == "\n":
                yield res
                res = ""
            else:
                res += char


if __name__ == "__main__":
    a = print_file("my_f.txt")
    print(next(a))
    print(next(a))
    for i in a:
        print(i)
