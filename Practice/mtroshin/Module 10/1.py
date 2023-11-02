import re


with (open("README.md", 'r', encoding="UTF-8")) as source_file:
    s = source_file.read()
    
search_str = re.compile(r'git [a-z]+')
res = re.findall(search_str, s)
print(res)
