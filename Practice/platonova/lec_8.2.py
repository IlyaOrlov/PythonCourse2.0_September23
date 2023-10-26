def gener_string(file1):
    for line in file1:
        yield line


with open("text1.txt") as file1:
    for line in gener_string(file1):
        print(line.strip())