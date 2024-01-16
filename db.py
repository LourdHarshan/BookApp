import sqlite3
con = sqlite3.connect("Books.db")
cursor = con.cursor()
cursor.execute("select * from books")
for i in cursor.fetchall():
    print(i)
