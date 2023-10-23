import re
# with open("log_file.txt") as f:
#     for line in f:
#        if "ERROR-" in line:
#            pos = line.find("ERROR-")
#            buf = ""
#            while line[pos] != " ":
#                buf += line[pos]
#                pos += 1
#            print(buf)

lst = []
with open("log_file.txt") as f:
    ptn = re.compile(r"(ERROR-[0-9]*)")
    for line in f:
       lst.extend(re.findall(ptn, line))

print(lst)

