import re


lst = []

with open(r"..\README.md", encoding="utf-8") as f:
    for line in f:
        l1 = re.findall(r"(git c.{5,7} [^\"]*)", line)
        if l1:
            lst += l1
        l2 = re.findall(r"(git \w{3,5} [^()\"1]*)", line)
        if l2:
            lst += l2

for i in lst:
    print(i)
