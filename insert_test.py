import sqlite3

con = sqlite3.connect("knowledge.db")
cur = con.cursor()

cur.execute("""
INSERT INTO methods (name,description,category,memo)
VALUES ('Flask','ルーティングの基本','python','最初のてすと')
            """)

con.commit()
con.close()

print("テスト完了")