import sqlite3
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
            if params:
                cursor.execute(query, *params)
            else:
                cursor.execute(query)
            rows = cursor.fetchall()
            columns = [column[0] for column in cursor.description]
            results = []
            for row in rows:
                res = {}
                for i in range(len(columns)):
                    res[columns[i]] = row[i]
                results.append(res)
            return results
        except sqlite3.Error as e:
            return {"STATUS": "ERROR", "MESSAGE": str(e)}

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
        data = db.read('SELECT * FROM Car')
        print(json.dumps(data))
