s = {2, 3, 4, "abc", 7, "x"}
s.add(100500)
print(s)

lst = [1, 2, 4, 5, 8, 2, 4]
lst = list(frozenset(lst))
print(lst)

s1 = {"Иванов", "Петров", "Сидоров"}
s2 = {"Иванов", "Шапкин", "Тапкин"}
company = {frozenset(s1), frozenset(s2)}
print(company)

for i in company:
    print(i)
