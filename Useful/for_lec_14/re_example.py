import re

s = "Всем привет, Всем пока bbb!"
# res = s.replace("В", "*").replace("в", "*").replace("B", "*").replace("b", "*")
# print(res)

res = re.sub(" .?", " *", s, flags=re.I)
print(res)