def gener_string(file1):
    for line in file1:
        yield line


with open("myfile1.txt") as f:
    for x in gener_string(f):
        print(x)
