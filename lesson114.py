import sqlite3 as sq

#con = sq.connect('profile1.db') # подключение к базе данных
#cur = con.cursor() # соединение к управлению данными

# запись запросов
#cur.execute('''
#''')

# закрытие базы данных
#con.close()

with sq.connect('profile1.db') as con:
    cur = con.cursor()
    #cur.execute('''CREATE TABLE IF NOT EXISTS users(
    #id INTEGER PRIMARY KEY AUTOINCREMENT,
    #name TEXT NOT NULL,
    #summa REAL,
    #data BLOB
     # )'''
    cur.execute('DROP TABLE users')


