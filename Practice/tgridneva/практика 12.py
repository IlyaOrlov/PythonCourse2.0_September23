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
        cursor = self.connection.cursor()
        cursor.execute(query)
        columns = [column[0] for column in cursor.description]
        rows = cursor.fetchall()
        results = []
        for row in rows:
            results.append(dict(zip(columns, row)))
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
