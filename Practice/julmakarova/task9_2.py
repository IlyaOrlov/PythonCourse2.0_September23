import datetime as dt


class Holidays:
    HOLIDAYS = frozenset([dt.date(2023, 2, 23), dt.date(2023, 3, 8),
                          dt.date(2023, 6, 12), dt.date(2023, 11, 4),
                          dt.date(2023, 12, 31)])

    def __init__(self):
        self._set_hol = Holidays.HOLIDAYS

    @property
    def set_hol(self):
        return self._set_hol

    def add_holiday(self, h_day, duration):
        if isinstance(self._set_hol, frozenset):
            self._set_hol = set(self._set_hol)
        for i in range(0, duration):
            n_hol = h_day + dt.timedelta(days=i)
            self._set_hol.add(n_hol)


def work_days(start_date, stop_date, holidays):
    w_days = 0
    i_date = start_date
    while i_date != stop_date:
        if i_date.weekday() < 5 and i_date not in holidays:
            w_days += 1

        i_date += dt.timedelta(days=1)

    return w_days


holiday = Holidays()
holiday.add_holiday(dt.date(2023, 1, 1), 8)
holiday.add_holiday(dt.date(2023, 5, 1), 9)

d1 = dt.date(2023, 1, 1)
d2 = dt.date(2023, 1, 13)

print(f"Количество рабочих дней между заданными датами: {work_days(d1, d2, holiday.set_hol)}")

