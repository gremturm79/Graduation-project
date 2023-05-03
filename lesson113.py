import sqlite3 as sq

#con = sq.connect('profile.db')
#cur = con.cursor()  # метод объекта соединения

#cur.execute('''
#''')

#con.close()

with sq.connect('profile.db') as con:
    cur = con.cursor()
    cur.execute('''CREATE TABLE IF NOT EXISTS users(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    summa REAL,
    data BLOB
    )''')
    cur.execute('DROP TABLE users')


