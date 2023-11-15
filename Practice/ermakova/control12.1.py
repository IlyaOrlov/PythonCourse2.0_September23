import sqlite3
import os
import json


class ClassWrapper:
    def __init__(self, dbname):
        self.dbname = dbname
        self._conn = sqlite3.connect(dbname)

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self._conn.close()

    def read(self, query, *params):
        cursor = self._conn.cursor()
        try:
            cursor.row_factory = sqlite3.Row
            if params:
                cursor.execute(query, *params)
            else:
                cursor.execute(query)
            results = [dict(row) for row in cursor.fetchall()]
            return {"STATUS": "SUCCESS", "RESULT": results, "MESSAGE": None}
        except sqlite3.Error as e:
            return {"STATUS": "ERROR", "RESULT": None, "MESSAGE": str(e)}

    def write(self, query, *params):
        try:
            cursor = self._conn.cursor()
            cursor.execute(query, *params)
            self._conn.commit()
            return "MESSAGE: SUCCESSFUL"
        except sqlite3.Error as e:
            return f"MESSAGE: {e}"


if __name__ == "__main__":
    db_name = "Car.db"
    if not os.path.exists(db_name):
        cars = ("CREATE TABLE IF NOT EXISTS Car"
                "(Id        INTEGER    PRIMARY KEY  AUTOINCREMENT,"
                " Brand     CHAR(128)  NOT NULL,"
                " Price     INTEGER    DEFAULT 0,"
                " Color     CHAR(128)  NOT NULL);")
        with ClassWrapper(db_name) as db:
            d = db.write(cars)
            result = db.write("INSERT INTO Car (ID, Brand, Price, Color)"
                              " VALUES (?, ?, ?, ?)", (1, 'BMW', 10000.00, 'RED'))
            print(result)
    else:
        with ClassWrapper(db_name) as db:
            data = db.read('SELECT * FROM Car')
            print(json.dumps(data))
