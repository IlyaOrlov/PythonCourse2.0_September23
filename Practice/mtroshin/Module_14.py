# Написать класс-обертку над SQLite (с возможностями менеджера контекста),
# которая может на вход принимать строки SQL запросов и возвращать данные в формате json.
# Класс должен иметь, как минимум, методы select и execute.

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
    db_name = "User.db"
    users = ("CREATE TABLE IF NOT EXISTS User"
             "(Id        INTEGER    PRIMARY KEY  AUTOINCREMENT,"
             " Name     CHAR(128)  NOT NULL,"
             " Salary     INTEGER    DEFAULT 0,"
             " City     CHAR(128)  NOT NULL);")
    with ClassWrapper(db_name) as db:
        d = db.write(users)
        result = db.write("INSERT INTO User (Name, Salary, City)"
                          " VALUES (?, ?, ?)", ('Anna', 10000.00, 'Orel'))
        result = db.write("INSERT INTO User (Name, Salary, City)"
                          " VALUES (?, ?, ?)", ('Anatoliy', 1000000.00, 'Moscow'))
        print(result)
        final_data = db.read('SELECT Id, Name, Salary FROM User')
        print(json.dumps(final_data))

