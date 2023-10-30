import re

lst = []
with open(r"..\..\README.md", "r", encoding="utf-8") as f:
    x = re.compile(r'git\s+[a-z]*', re.I)
    for line in f:
        line = line.rstrip('\n')
        lst += re.findall(x, line)

if __name__ == "__main__":
    for i in lst:
        print(i)
