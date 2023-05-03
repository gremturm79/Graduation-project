import sqlite3 as sq

with sq.connect(r'C:\Users\Alex\Desktop\Dat_b\db_7.db') as con:
    cur = con.cursor()
    cur.execute('''
    SELECT MAX(raiting)
    FROM Customers
    GROUP BY city
    ''')
    res = cur.fetchall()