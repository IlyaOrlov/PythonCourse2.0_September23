from datetime import datetime, timedelta


def count_working_days(start_date, end_date):
    start_date = datetime.strptime(start_date, "%Y-%m-%d")
    end_date = datetime.strptime(end_date, "%Y-%m-%d")

    holidays = [
        datetime(2023, 1, 1),
        datetime(2023, 3, 8),
        datetime(2023, 5, 1),
        datetime(2023, 5, 9),
        datetime(2023, 6, 12),
        datetime(2023, 11, 4),
    ]

    working_days = 0

    current_date = start_date
    while current_date <= end_date:
        if current_date.weekday() < 5 and current_date not in holidays:
            working_days += 1

        current_date += timedelta(days=1)
    return working_days


start_date = "2023-01-01"
end_date = "2023-01-31"

result = count_working_days(start_date, end_date)
print("Количество рабочих дней:", result)
