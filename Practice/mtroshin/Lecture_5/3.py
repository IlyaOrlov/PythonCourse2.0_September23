s = input("Как твои дела? Напиши: ")
# s1 = s.replace("h", "H").replace("ll", "LL")

slovar = {"плохо": "слава Богу!", "ужасно": "слава Всевышнему!", "так себе": "слава Богу", "хорошо": "слава Господу", "отлично": "слава Богу", "сложно": "с Божьей Помощью"}

for k, v in slovar.items():
    s = s.replace(k, v)

print(f"Значит: {s} ;)")