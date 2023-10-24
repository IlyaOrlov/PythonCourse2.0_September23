import datetime


def count_working_days(start_date, end_date):
    holidays = [
        datetime.date(2023, 1, 1),
        datetime.date(2023, 3, 8),
        datetime.date(2023, 5, 1),
    ]

    working_days = 0

    current_date = start_date
    while current_date <= end_date:
        if current_date.weekday() < 5 and current_date not in holidays:
            working_days += 1
        current_date += datetime.timedelta(days=1)

    return working_days


start_date = datetime.date(2023, 1, 1)
end_date = datetime.date(2023, 1, 10)
result = count_working_days(start_date, end_date)
print(result)
