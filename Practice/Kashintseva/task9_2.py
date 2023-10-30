import datetime as dt


def working_days(d1, d2):
    wd = 0
    while d1 <= d2:
        if d1.weekday() < 5:
            wd += 1
        d1 += dt.timedelta(days=1)
    return wd


st = dt.datetime(2023, 7, 1)
end = dt.datetime(2023, 7, 31)
w_days = working_days(st, end)
print(f"Рабочих дней: {w_days}")
