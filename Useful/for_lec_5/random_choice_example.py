# Написать генератор имён из 5 букв
import random


s1 = "вбгдк"
s2 = "аеуо"
name = random.choice(s1).upper() + random.choice(s2) + random.choice(s1) + random.choice(s2)
print(name)
