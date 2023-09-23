d = {"Mon": "Понедельник", "Tue": "Вторник", "Wed": "Среда", "Thu": "Четверг", "Fri": "Пятница"}
s = ("Часы работы:\n 13-17 - Mon, Thu, Fri\n 9-13 - Tue, Wed")
for k, v in d.items():
    s = s.replace(k, v)
print(s)
