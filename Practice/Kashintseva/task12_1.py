import os
import sqlite3
import json


class DBC:
    def __init__(self, d):
        self._conn = sqlite3.connect(d)

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self._conn.close()

    def info(self, call, param):
        cur = self._conn.cursor()
        cur.row_factory = sqlite3.Row
        cur.execute(call, param)
        for row in cur.fetchall():
            return json.dumps(dict(row))

    def changes(self, call, param):
        cur = self._conn.cursor()
        cur.execute(call, param)
        self._conn.commit()
        return bool(cur.fetchone())


if __name__ == "__main__":
    data = "childrengr.db"
    with DBC(data) as db:
        child_id = int(input("Введите номер ребенка в списке: "))
        res = db.info("SELECT * FROM Children AS C WHERE C.Id = :child_id", {"child_id": child_id})
        print(res)
        new_height = input("Введите новое значение роста ребенка: ")
        if new_height.isdecimal:
            new = db.changes("UPDATE Children "
                             "SET Height = :new_height "
                             "WHERE Id = :child_id ",
                             {'сhild_id': child_id, 'new_height': new_height})
            print(json.dumps({"Изменение данных": "успешно"}))
        else:
            print(json.dumps({"Изменение данных": "ошибка ввода. Данные изменить не удалось"}))
