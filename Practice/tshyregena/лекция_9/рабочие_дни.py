import datetime as dt


def fun(weekday, time):
    res = []
    i = 1
    t = time
    w = weekday
    while i <= t:
        w3 = w.strftime("%w")
        i += 1
        w = w + dt.timedelta(days=1)
        if 0 < int(w3) <= 5:
            res.append(w3)
        else:
            pass
    return len(res)


y1 = int(input("Введите год первой даты в формате 'YYYY': "))
m1 = int(input("Введите месяц первой даты в формате 'M': "))
d1 = int(input("Введите день первой даты в формате 'D': "))
weekday1 = dt.datetime(y1, m1, d1)
print(f'{weekday1} это {weekday1.strftime("%A")}')
y2 = int(input("Введите год первой даты в формате 'YYYY': "))
m2 = int(input("Введите месяц первой даты в формате 'M': "))
d2 = int(input("Введите день первой даты в формате 'D': "))
weekday2 = dt.datetime(y2, m2, d2)
time3 = (weekday2 - weekday1).days
print(f"С начальной даты до конечной {fun(weekday1, time3)} рабочих дня")
