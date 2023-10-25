import re


with open("../README.md", "r", encoding="utf-8") as file:
    lst = []
    for line in file:
        x = (re.findall(r'git\s+[a-z]+[^а-я()"]*', line, re.I))
        lst += x

for i in lst:
    print(i)
