from datetime import datetime, timedelta


def work_day(start, end):
    work = 0
    curr_date = start
    while curr_date <= end:
        if curr_date.weekday() < 5:
            work += 1
        curr_date += timedelta(days=1)
    return work


start_date, end_date = datetime(2023, 1, 1), datetime(2023, 12, 31)
print(f"В этом промежутке времни надо было отработать минимум: {work_day(start_date, end_date)} дней")
