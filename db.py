# db.py
""" Module to store data  in a database and retrieve it """

import sqlite3

conn = sqlite3.connect("time_logs.db")

cur = conn.cursor()
cur.execute("""
    CREATE TABLE time_logs (
        id  INTEGER PRIMARY KEY,
        project TEXT NOT NULL,
        date  TEXT NOT NULL,
        start_time TIME NOT NULL,
        end_time TEXT NOT NULL,
        duration  REAL NOT NULL
    )
""")

