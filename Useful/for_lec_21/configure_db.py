import os
import sqlite3


def configure_db(conn):
    cur = conn.cursor()

    # Создаем таблицу Employees
    cur.execute("CREATE TABLE Details"
                "    (Id        INTEGER    PRIMARY KEY  AUTOINCREMENT,"
                "     Name      CHAR(128)  NOT NULL,"
                "     Price     INTEGER    DEFAULT 0,"
                "     Num       INTEGER    DEFAULT 0)")


def initial_fill(conn):
    cur = conn.cursor()
    cur.execute("INSERT INTO Details (Name, Price, Num) VALUES ('гайка', 10, 100)")
    cur.execute("INSERT INTO Details (Name, Price, Num) VALUES ('гвоздь', 10, 100)")
    cur.execute("INSERT INTO Details (Name, Price, Num) VALUES ('болт', 10, 100)")
    conn.commit()


if __name__ == "__main__":
    db_name = "mydetails.db"
    if not os.path.exists(db_name):
        conn = sqlite3.connect(db_name)
        configure_db(conn)
        initial_fill(conn)