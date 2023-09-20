def print_file(file):
    with open(file, "r", encoding="utf-8") as f:
        print(f.read())


def replace_char_file(file, old_char, new_char):
    with open(file, "r", encoding="utf-8") as f:
        text = f.read().replace(old_char, new_char)
    with open(file, "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    with open("my_f.txt", "w", encoding="utf-8") as new_f:
        new_f.write("1    2    3    4    5")
    print_file("my_f.txt")
    replace_char_file("my_f.txt", "    ", "\\t")
    print_file("my_f.txt")
    replace_char_file("my_f.txt", "\\t", "    ")
    print_file("my_f.txt")
