import sqlite3
import os
import json


class SQLtoJson:
    def __init__(self, db):
        self._conn = sqlite3.connect(db)

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self._conn.close()

    def select(self, req, param=None):
        cur = self._conn.cursor()
        if param:
            cur.execute(req, param)
        else:
            cur.execute(req)
        return json.dumps(cur.fetchall())

    def execute(self, req, param=None):
        cur = self._conn.cursor()
        if param:
            cur.execute(req, param)
        else:
            cur.execute(req)
        try:
            self._conn.commit()
            r_value = True
        except Exception as e:
            print(f"Запрос не выполнен. Возникло исключение: {e}.")
            r_value = False

        return json.dumps(r_value)


if __name__ == "__main__":
    name_db = "test_db.db"

    if not os.path.exists(name_db):
        with SQLtoJson(name_db) as r:
            r.execute("CREATE TABLE Car (Id INTEGER PRIMARY KEY AUTOINCREMENT, Name CHAR(128) NOT NULL,"
                      "Speed INTEGER DEFAULT 0, Consum INTEGER DEFAULT 0)")
            r.execute("INSERT INTO Car (Name, Speed, Consum) VALUES ('Voyah', 250, 9)")
            r.execute("INSERT INTO Car (Name, Speed, Consum) VALUES ('Exeed', 230, 17)")
            r.execute("INSERT INTO Car (Name, Speed, Consum) VALUES ('Zeekr', 280, 7)")
            r.execute("INSERT INTO Car (Name, Speed, Consum) VALUES ('Lixiang', 280, 9)")
    else:
        with SQLtoJson(name_db) as r:
            print(r.select("SELECT * FROM Car"))
            print(r.select("SELECT * FROM Car AS C WHERE C.Speed = :sp", {'sp': 280}))

