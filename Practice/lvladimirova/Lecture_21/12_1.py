import sqlite3
import json


class SQLiteWrapper:
    def __init__(self, db_file):
        self.db_file = db_file

    def __enter__(self):
        self.conn = sqlite3.connect(self.db_file)
        self.cursor = self.conn.cursor()
        self.create_users_table()
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.conn.close()

    def create_users_table(self):
        self.cursor.execute("CREATE TABLE IF NOT EXISTS users"
                            "    (Id        INTEGER    PRIMARY KEY,"
                            "     Name      TEXT       NOT NULL,"
                            "     Age       INTEGER    NOT NULL)")
        self.conn.commit()

    def read(self, query, *params):
        self.cursor.execute(query, params)
        self.cursor.row_factory = sqlite3.Row
        data = [dict(row) for row in self.cursor.fetchall()]
        return json.dumps(data)

    def write(self, query, *params):
        try:
            self.cursor.execute(query, params)
            self.conn.commit()
            return json.dumps({"Статус": "Успех!", "Сообщение": "Операция выполнена успешно!"})
        except Exception as e:
            return json.dumps({"Статус": "Ошибка!", "Сообщение": f"Произошла ошибка: {e}"})


if __name__ == "__main__":
    my_db_file = 'proba.db'
    with SQLiteWrapper(my_db_file) as db:
        result_json = db.read("SELECT * FROM users")
        print(result_json)
        while (input_data := input("Введите имя или 'стоп' для завершения: ")) != 'стоп':
            age = input("Введите возраст: ")
            if age.isdecimal():
                write_result_json = db.write("INSERT INTO users (name, age) VALUES (?, ?)", input_data, int(age))
                print(write_result_json)
            else:
                print("Неправильный формат возраста. Пожалуйста, введите число.")
