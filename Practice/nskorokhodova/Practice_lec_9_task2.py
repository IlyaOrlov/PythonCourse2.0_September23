path_to_file = "C:\Python\python.exe\Files\info.txt"
with open(path_to_file) as file:
    for num_line, line in enumerate(file):
        print(num_line, line)
