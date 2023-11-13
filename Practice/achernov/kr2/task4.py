# def copyfile(source, destination):
#     try:
#         with open(source) as s:
#             text = s.read()
#     except FileNotFoundError:
#         print(f"File for read not found!")
#         return None
#     try:
#         with open(destination, "x") as d:
#             d.write(text)
#             print("Copy successful!")
#     except FileExistsError:
#         print(f"File already exists!")
#
#
# copyfile("test_source.txt", "test_destination.txt")
def copyfile(s, d):
    try:
        with open(s, "r") as f:
            text = f.read()
    except FileNotFoundError:
        print(f"File for read not found!")
        return None
    try:
        with open(d, "x") as f:
            f.write(text)
            print("Copy successful!")
    except FileExistsError:
        print(f"File already exists!")


copyfile("test_source.txt", "test_destination.txt")
