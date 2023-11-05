import datetime as dt

def working_days(start_date, end_date):
    count = 0
    current_date = start_date

    while current_date <= end_date:
        if current_date.weekday() < 5:
            count += 1
        current_date += dt.timedelta(days=1)

    return count


start_date = dt.date(2023, 10, 1)
end_date = dt.date(2023, 10, 5)

print(f"количество рабочих дней между двумя датами: {working_days(start_date, end_date)}")
