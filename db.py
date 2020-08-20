import sqlite3


class DataBase:
    def __init__(self, db):
        self.conn = sqlite3.connect(db)
        self.cur = self.conn.cursor()
        self.cur.execute(
            """CREATE TABLE IF NOT EXISTS data (ID INTEGER PRIMARY KEY, fname TEXT, sname TEXT,
                email TEXT, number TEXT, major TEXT, gpa TEXT, year NUMERIC, gender TEXT)""")
        self.conn.commit()

    def fetch(self):
        self.cur.execute("SELECT * FROM data")
        rows = self.cur.fetchall()
        return rows

    def fetchone_f(self, ID):
        self.cur.execute("SELECT * FROM data WHERE ID = ?", (ID,))
        row = self.cur.fetchone()
        return row

    def insert(self, fname, sname, email, number, major, gpa, year, gender):
        self.cur.execute("INSERT INTO data VALUES(NULL, ? , ?, ?, ?, ?, ?, ?, ?)",
                         (fname, sname, email, number, major, gpa, year, gender))
        self.conn.commit()

    def remove(self, ID):
        self.cur.execute("DELETE FROM data WHERE ID=?", (ID,))
        self.conn.commit()

    def update(self, ID, fname, sname, email, number, major, gpa, year, gender):
        self.cur.execute("UPDATE data SET fname = ?, sname = ?, email = ?, number = ?, major = ?, gpa = ?, year = ?, gender = ? WHERE ID = ?",
                         (fname, sname, email, number, major, gpa, year, gender, ID))
        self.conn.commit()

    def __del__(self):
        self.conn.close()


db = DataBase("data.db")
