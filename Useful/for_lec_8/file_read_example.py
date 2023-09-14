# file1 = open("myfile.txt", encoding="utf-8")
# # s = file1.read()
# # print(s)
# for s in file1:
#     print(s)
# file1.close()

with open("myfile.txt", encoding="utf-8") as file1:
    for s in file1:
        print(s)

