import sqlite3 as sq

with sq.connect(r'C:\Users\Alex\Desktop\DB1\DB\DB_2\db_3.db') as con:
    cur = con.cursor()
    cur.execute('''
    SELECT *
    FROM T1
    ORDER BY FName
    LIMIT 2, 5
    ''')

    res = cur.fetchone()
    res2 = cur.fetchmany()
    print(res)
    print(res2)
    #res = cur.fetchall()
    #print(res)



