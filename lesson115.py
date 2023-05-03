import sqlite3 as sq

with sq.connect('users1.db') as con:
    cur = con.cursor()
    cur.execute('''
    DROP TABLE person_table
    ''')

    # cur.execute('''
    # CREATE TABLE IF NOT EXISTS person(
    # Id INTEGER PRIMARY KEY AUTOINCREMENT,
    # name TEXT NOT NULL,
    # phone BLOB NOT NULL DEFAULT '+79006548563',
    # age INTEGER NOT NULL CHECK(age>15 AND age<70),
    #email TEXT UNIQUE
    # )''')
