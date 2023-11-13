import os
import sqlite3


class DBClient:
    def __init__(self, dbname):
        self._conn = sqlite3.connect(dbname)

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self._conn.close()

    def get_detail(self, detail_id):
        cur = self._conn.cursor()
        cur.execute("SELECT * FROM Details AS D WHERE D.Id = :id", {'id': detail_id})
        return cur.fetchone()


if __name__ == "__main__":
    db_name = "mydetails.db"
    with DBClient(db_name) as db_client:
        while d := input("Введите id детали: "):
            res = db_client.get_detail(int(d))
            if res:
                print(res)
            else:
                print("Такой детали нет")

