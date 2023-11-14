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
        self.cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        age INTEGER
        )''')
        self.conn.commit()

    def read(self, query, *params):
        self.cursor.execute(query, params)
        columns = [column[0] for column in self.cursor.description]
        data = [dict(zip(columns, row)) for row in self.cursor.fetchall()]
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
        age = 0
        while (input_data := input("Введите имя (введите 'стоп' для завершения): ")) != 'стоп':
            while True:
                try:
                    age = int(input("Введите возраст: "))
                    break
                except ValueError:
                    print("Неправильный формат возраста. Пожалуйста, введите число.")
                    write_result_json = db.write("INSERT INTO users (name, age) VALUES (?, ?)", input_data, age)
                    print(write_result_json)
