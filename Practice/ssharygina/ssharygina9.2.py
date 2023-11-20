import datetime


def rab_day(d1, d2):
    start = d1 if d1 < d2 else d2
    res = 0
    for _ in range(abs(d2 - d1).days):
        if start.isoweekday() < 6:
            res += 1
        start += datetime.timedelta(days=1)
    print(f"Между двумя датами прошло дней: {abs(d2 - d1).days}, из них рабочих: {res}, а остальные - выходные!")


if __name__ == "__main__":
    try:
        rab_day(datetime.date(2023, 1, 1), datetime.date(2023, 11, 3))
    except ValueError:
        print("Ошибка! Некорректно заданы даты!")
