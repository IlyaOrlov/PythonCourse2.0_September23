def copyfile(source, destination):
    try:
        with open(source) as s:
            text = s.read()
    except FileNotFoundError:
        print(f"File for read not found!")

    try:
        with open(destination, "x") as d:
            d.write(text)
            print("Copy successful!")
    except FileExistsError:
        print(f"File already exists!")


copyfile("exam_test.txt", "exam_des1.txt")


