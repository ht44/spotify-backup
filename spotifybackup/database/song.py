import os
import sqlite3


def get_songs():
    conn = sqlite3.connect(os.getenv('DB_PATH'))
    c = conn.cursor()
    result = c.execute('''SELECT * FROM song''').fetchall()
    conn.commit()
    conn.close()
    return result


def get_song(song_id):
    conn = sqlite3.connect(os.getenv('DB_PATH'))
    c = conn.cursor()
    t = (song_id,)
    result = c.execute('SELECT * FROM song WHERE id=?', t).fetchone()
    conn.close()
    return result
