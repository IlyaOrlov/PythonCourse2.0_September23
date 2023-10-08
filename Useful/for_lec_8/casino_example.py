import random


values = ("лимон", "доллар", "вишенка")
while input() != "stop":
    print(f"{random.choice(values)}|{random.choice(values)}|{random.choice(values)}")
