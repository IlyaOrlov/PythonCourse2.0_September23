# file1 = open("myfile.txt", encoding="utf-8")
# # s = file1.read()
# # print(s)
# for s in file1:
#     print(s)
# file1.close()
t = input("напиши цифру 1 или 2\n1 - для замены пробелов на знак табуляции,\n2 (или любое, кроме 1) - для замены знаков табуляции на пробелы:\n")

with open("file.txt", "r", encoding="utf-8") as file1:
    filedata = file1.read()

if t == "1":
    filedata = filedata.replace('    ','\t')
else:
    filedata = filedata.replace('\t', '    ')

with open("file.txt", "w", encoding="utf-8") as file1:
    file1.write(filedata)