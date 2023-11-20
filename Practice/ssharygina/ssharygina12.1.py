import sqlite3
import json


class MySQLiteWrap:
    def __init__(self, dbname):
        self._connection = sqlite3.connect(dbname)

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self._connection.close()

    def config(self):
        print(f"Создается таблица Films, если она еще не существует")
        cursor = self._connection.cursor()
        tabl = ("CREATE TABLE IF NOT EXISTS Films"
                "(Id      INTEGER    PRIMARY KEY  AUTOINCREMENT,"
                " Name    CHAR(128)  NOT NULL,"
                " Series  INTEGER    DEFAULT 1,"
                " Type    CHAR(128)  NOT NULL);")
        cursor.execute(tabl)
        self._connection.commit()

    def insert(self):
        print(f"Добавление стороки в таблицу Films")
        cursor = self._connection.cursor()
        tabl = "INSERT INTO Films (Name, Series, Type) VALUES (?, ?, ?)"
        cursor.execute(tabl,  (input("Название: "), input("Кол-во серий (частей): "), input("Тип: ")))
        self._connection.commit()

    def select(self):
        print("Вывод на экран таблицы Films:")
        cursor = self._connection.cursor()
        print(json.dumps(cursor.execute("SELECT * from Films").fetchall()))


if __name__ == "__main__":
    with MySQLiteWrap('Films.db') as db:
        db.config()
        db.insert()
        db.select()
