from datetime import datetime, timedelta


def qol(start, end):
    num = 0
    current_date = start
    while current_date <= end:
        if current_date.weekday() < 5:
            num += 1
        current_date += timedelta(days=1)
    return num


if __name__ == "__main__":
    start_date, end_date = datetime(2023, 10, 1), datetime(2023, 10, 31)
    print(f"Количество рабочих дней: {qol(start_date, end_date)}")
