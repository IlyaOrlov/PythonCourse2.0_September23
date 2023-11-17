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
        return json.dumps([dict(row) for row in cur.fetchall()], ensure_ascii=False)

    def changes(self, call, param):
        cur = self._conn.cursor()
        cur.execute(call, param)
        try:
            self._conn.commit()
            return json.dumps({"Изменение данных": "успешно"}, ensure_ascii=False)
        except Exception as e:
            return json.dumps({f'"Изменение данных": "ошибка {e}."'}, ensure_ascii=False)


if __name__ == "__main__":
    data = "childrengr.db"
    with DBC(data) as db:
        child_id = int(input("Введите номер ребенка в списке: "))
        res = db.info("SELECT * FROM Children AS C WHERE C.Id = :child_id", {"child_id": child_id})
        print(res)
        new_height = input("Введите новое значение роста ребенка: ")
        if new_height.isdecimal():
            new = db.changes("UPDATE Children "
                             "SET Height = :new_height "
                             "WHERE Id = :child_id ",
                             {'child_id': child_id, 'new_height': new_height})
            print(new)
        else:
            print(json.dumps({"Изменение данных": "не успешно. Введено не число"}, ensure_ascii=False))
