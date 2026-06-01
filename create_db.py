import sqlite3
con = sqlite3.connect("knowledge.db")

cur = con.cursor()

cur.execute("""
CREATE TABLE methods (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    description TEXT,
    category TEXT,
    memo TEXT
)
""")

con.commit()
con.close()

print("DB作成完了")