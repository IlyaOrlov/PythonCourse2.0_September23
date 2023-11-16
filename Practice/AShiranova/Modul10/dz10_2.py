import datetime as dt


def long_work(d1, d2):
    start = d1 if d1 < d2 else d2
    res = 0
    for _ in range(abs(d2 - d1).days):
        if start.isoweekday() < 6:
            res += 1
        start += dt.timedelta(days=1)
    print(f"Всего дней {abs(d2 - d1).days} из них рабочих {res}")


if __name__ == "__main__":
    try:
        long_work(dt.date(1993, 1, 1), dt.date(1993, 12, 31))
    except ValueError:
        print("Ошибка. Введите корректное значение.")
