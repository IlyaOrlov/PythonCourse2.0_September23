import re


search_str = re.compile(r'git [a-z]+')
lst = []
with open("README.md", 'r', encoding="UTF-8") as source_file:
    for line in source_file:
        lst.extend(re.findall(search_str, line))
print(lst)
