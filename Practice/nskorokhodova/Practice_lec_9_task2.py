def read_file(file_path):
    with open(file_path, 'r') as file:
        for line in file:
            yield line.rstrip('\n')

file_path = 'C:\Python\python.exe\..\Files\info.txt'
for line in read_file(file_path):
    print(line)
