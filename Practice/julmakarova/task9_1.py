import re


lst = []

with open(r"..\README.md", encoding="utf-8") as f:
    pat1 = re.compile(r"(git c.{5,7} [^\"]*)")
    pat2 = re.compile(r"(git \w{3,5} [^()\"1]*)")
    for line in f:
        lst += re.findall(pat1, line) + re.findall(pat2, line)

for i in lst:
    print(i)
