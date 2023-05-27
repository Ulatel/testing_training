import sqlite3

def insert_into_db(id, target, value):
    id = int(id)
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    array = conn.execute('SELECT * FROM arrays WHERE id = ?',
                        (id,)).fetchone()
    if array==None:
        conn.execute('INSERT INTO arrays (id, title, content) VALUES (?, ?, ?)',
                 (id, target, value))
    else:
        conn.execute('UPDATE arrays SET title = ?, content = ?'
                    ' WHERE id = ?',
                (target, value, id))
    conn.commit()
    conn.close()



