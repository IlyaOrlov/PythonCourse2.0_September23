import datetime as dt


def long_work(d1, d2):
    start = d1 if d1 < d2 else d2
    res = 0
    for _ in range(abs(d2 - d1).days):
        if start.isoweekday() in (1, 2, 3, 4, 5):
            res += 1
        start = start + dt.timedelta(days=1)
    print(f"Всего дней {abs(d2 - d1).days} из них рабочих {res}")


if __name__ == "__main__":
    try:
        long_work(dt.date(1955, 2, 11), dt.date(1970, 1, 1))
    except ValueError:
        print("что то Вы напутали с датами, попробуйте еще раз")
