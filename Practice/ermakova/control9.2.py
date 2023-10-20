import datetime as dt
import holidays


def work_day(s, e):
    res = 0
    for i in range((e-s).days+1):
        day = s + dt.timedelta(i)
        if day.weekday() < 5:
            if day in holidays.country_holidays(country='RU'):
                pass
            else:
                res += 1
    return res


start = dt.datetime(2023, 1, 1)
end = dt.datetime(2023, 12, 31)
print(f"Количество рабочих дней в году: {work_day(start, end)}")
