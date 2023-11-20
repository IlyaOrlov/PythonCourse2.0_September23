import sqlite3
import json


class MySqlManager:
    def __init__(self, dbname):
        self._connection = sqlite3.connect(dbname)

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self._connection.close()

    def configure(self):
        print(f"CREATE TABLE IF NOT EXISTS User")
        cursor = self._connection.cursor()
        schema = ("CREATE TABLE IF NOT EXISTS User"
                  "    (Id          INTEGER    PRIMARY KEY  AUTOINCREMENT,"
                  "     First_name  CHAR(128)  NOT NULL,"
                  "     Last_name   CHAR(64)   NOT NULL,"
                  "     Age         CHAR(4)    DEFAULT '0')")
        cursor.execute(schema)
        self._connection.commit()

    def insert(self):
        print(f"INSERT INTO User")
        cursor = self._connection.cursor()
        schema = "INSERT INTO User (First_name, Last_name, Age) VALUES ( ?, ?, ? )"
        cursor.execute(schema,  (input("First_name: "), input("Last_name: "), input("Age: ")))
        self._connection.commit()

    def select_all(self):
        print("SELECT * from User")
        cursor = self._connection.cursor()
        print(json.dumps(cursor.execute("SELECT * from User").fetchall()))


if __name__ == "__main__":
    with MySqlManager('my_data.db') as db:
        db.configure()
        db.insert()
        db.select_all()
