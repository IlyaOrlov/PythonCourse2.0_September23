import re


lst = []
with open(r"..\..\README.md", "r", encoding="utf-8'") as f:
    reg = re.compile(r"git\s\w*")
    for line in f:
        line = line.rstrip('\n')
        lst += re.findall(reg, line)
    for i in lst:
        print(i)
