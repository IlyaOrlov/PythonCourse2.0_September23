import sqlite3
import json


class SQLiteWrapper:
    def __init__(self, db_file):
        self.db_file = db_file
        self.connection = None

    def __enter__(self):
        self.connection = sqlite3.connect(self.db_file)
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.connection:
            self.connection.close()

    def select(self, query):
        self.connection.row_factory = sqlite3.Row
        cursor = self.connection.cursor()
        cursor.execute(query)
        rows = cursor.fetchall()
        results = [dict(row) for row in rows]
        return json.dumps(results)

    def execute(self, query):
        cursor = self.connection.cursor()
        cursor.execute(query)
        self.connection.commit()


db_file = 'example.db'

create_table_query = '''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        age INTEGER NOT NULL
    )
'''

insert_data_query = '''
    INSERT INTO users (name, age) VALUES ('John', 25), ('Alice', 30), ('Bob', 35)
'''

select_data_query = '''
    SELECT * FROM users
'''

with SQLiteWrapper(db_file) as db:
    db.execute(create_table_query)
    db.execute(insert_data_query)
    result = db.select(select_data_query)
    print(result)
