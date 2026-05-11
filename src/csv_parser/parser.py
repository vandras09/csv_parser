import json
import sqlite3


def parse_to_db(file_path):
    file = open(file_path)
    con = sqlite3.connect("data.db")
    cur = con.cursor()
    cur.execute(f"CREATE TABLE message")
    for i in file[0]:
        cur.execute(f"ALTER TABLE message ADD {i}")
    for line in file:
        for i in line:
            cur.execute(f"INSERT INTO message VALUES {i}")

parse_to_db(".testfiles/test.csv")