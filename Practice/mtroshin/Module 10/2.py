import datetime as dt


def workdays_count(date1, date2):
    delta = date2 - date1
    ddays = delta.days
    print(f"Всего дней между ними {ddays}")
    workdays = 0
    while ddays > 0:
        if date1.weekday() < 5:
            workdays += 1
        date1 += dt.timedelta(days=1)
        ddays -= 1
    return workdays


date1 = dt.date(2023, 2, 18)
date2_now = dt.datetime.now()
date2 = date2_now.date() # странно почему не получается сделать сразу так? : date2 = dt.datetime.now().date()
print(f"Всего рабочих дней между датами: {workdays_count(date1, date2)}")
