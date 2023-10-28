import re


with open("D:\Мои файлы\PythonCourse2.0_September23\Practice\README.md", "r", encoding="utf-8") as f:
    pat = re.compile("git\s\w*")
    for line in f:
        if com := re.findall(pat, line):
            print(com)
