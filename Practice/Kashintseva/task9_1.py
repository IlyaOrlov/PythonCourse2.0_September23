import re


with open("D:\Мои файлы\PythonCourse2.0_September23\Practice\README.md", "r", encoding="utf-8") as f:
    for line in f:
        com = re.findall(r'(git\s\w*)', line)
        if com:
            print(com)
