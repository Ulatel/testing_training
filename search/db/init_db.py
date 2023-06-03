import sqlite3

connection = sqlite3.connect('database.db')


with open('search/db/schema.sql') as f:
    connection.executescript(f.read())

cur = connection.cursor()

cur.execute("INSERT INTO arrays (title, content) VALUES (?, ?)",
            ('First array', '1 2 3 4 5 6 7 8 9 -2 -1 0')
            )

cur.execute("INSERT INTO arrays (title, content) VALUES (?, ?)",
            ('Second array', '1')
            )

cur.execute("INSERT INTO secret (content) VALUES (?)",
            ('FfFflagg1asAsaaaa',)
            )

connection.commit()
connection.close()