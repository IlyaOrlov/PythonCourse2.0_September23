def my_gen(file):
    try:
        with open(file, "r") as file:
            for s in file:
                yield s
    except FileNotFoundError:
        print("Неправильный путь или такого файла не существует")


my_file = "test.txt"
for line in my_gen(my_file):
    print(line)
