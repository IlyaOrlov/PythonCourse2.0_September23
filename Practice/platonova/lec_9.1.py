import re


with open("..\README.md","r", encoding="utf-8") as file:
    pat = re.compile("git\s\w*")
    for line in file:
        if i := re.findall(pat, line):
            print(i)
