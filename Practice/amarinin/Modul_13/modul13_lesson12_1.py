import sqlite3


class MySqlManager:

    def __init__(self, db_name):
        self.db_name = db_name

    def __enter__(self):
        self.connection = sqlite3.connect(self.db_name)
        self.connection.row_factory = sqlite3.Row
        self.cursor = self.connection.cursor()
        print(f"Подключились к базе данных {self.db_name}\n")

    def __exit__(self, exc_type, exc_val, exc_tb):

        self.cursor.close()
        self.connection.close()
        print(f"\nБаза данных {self.db_name} закрыта")

    def create_table(self):
        print("Создаем таблицу")
        name_table = "CREATE TABLE " + input("Имя таблицы : ").lower().strip()
        name_prima = input("Имя поля первичного ключа : ").lower().strip() + " INTEGER PRIMARY KEY AUTOINCREMENT"
        name_fild1 = input("Имена полей через пробел : ").lower().strip().split()
        name_fild2 = [name_prima] + [i + " " + input(f"Тип поля {i}: ").upper().strip() for i in name_fild1]
        name_fild2 = " (" + ", ".join(name_fild2) + ")"
        schema = name_table + name_fild2
        self.cursor.execute(schema)
        self.connection.commit()
        print(f"{schema}\nТаблица создана\n")

    def insert_data(self):
        print("Вводим данные")
        self.cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
        table_name = input(f"Выбери таблицу: {[table[0] for table in self.cursor.fetchall()]}  :  ")
        column_name = self.cursor.execute(f"PRAGMA table_info({table_name})").fetchall()
        column_names = [col[1] for col in column_name]
        values_column = [input(f"Введите значение в поле {i}: ") for i in column_names[1:]]
        schema = f"INSERT INTO {table_name} ({', '.join(column_names[1:])}) VALUES ({', '.join(values_column)})"
        self.cursor.execute(schema)
        self.connection.commit()
        print(f"{schema}\nДанные введены\n")

    def update_data(self):
        pass

    def delete_data(self):
        pass

    def select(self):
        print("Запрос данных")
        self.cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
        table_name = input(f"Выбери таблицу: {[table[0] for table in self.cursor.fetchall()]}  :  ")
        column_name = self.cursor.execute(f"PRAGMA table_info({table_name})").fetchall()
        column_names = [col[1] for col in column_name]
        fields = input(f"Таблица '{table_name}', поля {column_names} Введите * или поля через запятую :  ")
        schema = f"SELECT {fields} from {table_name}"
        print(schema)
        res = self.cursor.execute(schema).fetchall()
        for s in res:
            for i in s:
                print(f"{i} ", end="")


if __name__ == "__main__":
    f = MySqlManager("my_data.db")
    with f:
        f.create_table()
        f.insert_data()
        f.select()
