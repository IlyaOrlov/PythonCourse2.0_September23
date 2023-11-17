import os
import sqlite3


def configure(conn):
    cur = conn.cursor()

    cur.execute("CREATE TABLE Children"
                "    (Id        INTEGER    PRIMARY KEY  AUTOINCREMENT,"
                "     Name      CHAR(128)  NOT NULL,"
                "     Age     INTEGER    DEFAULT 0,"
                "     Height    INTEGER    DEFAULT 0,"
                "     Weight    INTEGER    DEFAULT 0)")

    cur.execute("CREATE TABLE Gruppa"
                "   (Id     INTEGER     PRIMARY KEY     AUTOINCREMENT,"
                "   Name      CHAR(128)     NOT NULL,"
                "   Floor     INTEGER    DEFAULT 0)")

    cur.execute("CREATE TABLE ChildGrup"
                "    (ChildId  INTEGER,"
                "     GruppaId   INTEGER,"
                "     PRIMARY KEY (ChildId, GruppaId))")


def insert_children(conn):
    cur = conn.cursor()
    cur.execute("INSERT INTO Children (Name, Age, Height, Weight) VALUES ('Попов Миша', 2, 85, 15)")
    cur.execute("INSERT INTO Children (Name, Age, Height, Weight) VALUES ('Зотова Лера', 3, 100, 18)")
    cur.execute("INSERT INTO Children (Name, Age, Height, Weight) VALUES ('Кучина Лена', 2, 86, 14)")
    cur.execute("INSERT INTO Children (Name, Age, Height, Weight) VALUES ('Носков Артем', 4, 105, 20)")
    cur.execute("INSERT INTO Children (Name, Age, Height, Weight) VALUES ('Лосина Саша', 3, 98, 17)")
    conn.commit()


def insert_gruppa(conn):
    cur = conn.cursor()
    cur.execute("INSERT INTO Gruppa (Name, Floor) VALUES ('Zaiki', 1)")
    cur.execute("INSERT INTO Gruppa (Name, Floor) VALUES ('Luchiki', 2)")
    conn.commit()


def add_child_to_group(conn, child_id, gruppa_id):
    cur = conn.cursor()
    cur.execute("INSERT INTO ChildGrup (ChildId, GruppaId)"
                " VALUES (:childId, :gruppaId)",
                {'childId': child_id, 'gruppaId': gruppa_id})
    conn.commit()


if __name__ == "__main__":
    data = "childrengr.db"
    if not os.path.exists(data):
        conn = sqlite3.connect(data)
        configure(conn)
        insert_children(conn)
        insert_gruppa(conn)
        add_child_to_group(conn, 1, 1)
        add_child_to_group(conn, 2, 2)
        add_child_to_group(conn, 3, 1)
        add_child_to_group(conn, 4, 2)
        add_child_to_group(conn, 5, 2)
