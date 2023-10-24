import re

with open(r"..\README.md", encoding="utf-8") as f:
    all_text = f.read()

lst = re.findall(r"(git c.{5,7} [^\"]*)", all_text)
lst1 = re.findall(r"(git \w{3,5} [^()\"1]*)", all_text)
lst += lst1
for i in lst:
    print(i)
