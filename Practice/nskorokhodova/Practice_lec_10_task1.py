#Используя модуль re, найти все команды Git с аргументами в файле Practice/README.md
import re


lst = []
with open(r"C:\Users\..\Practice\README.md", "r", encoding="utf-8'") as f:
    reg = re.compile(r"git\s\w*")
    for line in f:
        line = line.rstrip('\n')
        lst += re.findall(reg, line)
    for i in lst:
        print(i)
