import os
import sqlite3


def get_albums():
    conn = sqlite3.connect(os.getenv('DB_PATH'))
    c = conn.cursor()
    result = c.execute('''SELECT * FROM album''').fetchall()
    conn.close()
    return result


def get_album(album_id):
    conn = sqlite3.connect(os.getenv('DB_PATH'))
    c = conn.cursor()
    t = (album_id,)
    result = c.execute('SELECT * FROM album WHERE id=?', t).fetchone()
    conn.close()
    return result

