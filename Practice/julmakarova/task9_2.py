import datetime as dt


def add_long_holiday(holiday, duration):
    for i in range(0, duration):
        n_hol = holiday + dt.timedelta(days=i)
        holidays.append(n_hol)


def work_days(start_date, stop_date):
    w_days = 0
    i_date = start_date
    while i_date != stop_date:
        if i_date.weekday() in range(0, 5) and not(i_date in holidays):
            w_days += 1

        i_date += dt.timedelta(days=1)

    return w_days


holidays = [dt.date(2023, 2, 23), dt.date(2023, 3, 8),
            dt.date(2023, 6, 12), dt.date(2023, 11, 4),
            dt.date(2023, 12, 31)]

add_long_holiday(dt.date(2023, 1, 1), 8)
add_long_holiday(dt.date(2023, 5, 1), 9)


d1 = dt.date(2023, 1, 1)
d2 = dt.date(2023, 1, 13)

print(f"Количество рабочих дней между заданными датами: {work_days(d1, d2)}")
