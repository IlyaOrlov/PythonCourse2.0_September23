import re


with open("../README.md", "r", encoding="utf-8") as file:
    lst = []
    s = re.compile(r'git\s+[a-z]+[^а-я()"]*', re.I)
    for line in file:
        line = line.rstrip('\n')
        lst += re.findall(s, line)

for i in lst:
    print(i)
