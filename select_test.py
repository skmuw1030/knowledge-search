import sqlite3

con = sqlite3.connect("knowledge.db")
cur = con.cursor()

cur.execute("SELECT * FROM methods")
rows = cur.fetchall()

for row in rows:
    print(row)

con.close()