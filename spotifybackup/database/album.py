import os
import sqlite3


def get_albums():
    conn = sqlite3.connect(os.getenv('DB_PATH'))
    c = conn.cursor()
    result = c.execute('''SELECT spotify_id, name FROM album''').fetchall()
    conn.close()
    return result


def get_album(album_id):
    conn = sqlite3.connect(os.getenv('DB_PATH'))
    c = conn.cursor()
    t = (album_id,)
    result = c.execute('SELECT * FROM album WHERE id=?', t).fetchone()
    conn.close()
    return result


def count_albums():
    conn = sqlite3.connect(os.getenv('DB_PATH'))
    c = conn.cursor()
    result = c.execute('SELECT COUNT(*) FROM album').fetchone()
    conn.close()
    return result


def search_albums(search=None):
    conn = sqlite3.connect(os.getenv('DB_PATH'))
    c = conn.cursor()
    query = """
        SELECT
          a.spotify_id, a.name
        FROM album AS a
        WHERE
          (?1 IS NULL OR a.name LIKE ?1 || '%')
    """
    result = c.execute(query, (search,)).fetchall()
    conn.close()
    return result
