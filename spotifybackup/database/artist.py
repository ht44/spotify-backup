import os
import sqlite3


def get_artists():
    conn = sqlite3.connect(os.getenv('DB_PATH'))
    c = conn.cursor()
    result = c.execute('''SELECT * FROM artist''').fetchall()
    conn.commit()
    conn.close()
    return result


def get_artist(artist_id):
    conn = sqlite3.connect(os.getenv('DB_PATH'))
    c = conn.cursor()
    t = (artist_id,)
    result = c.execute('SELECT * FROM artist WHERE id=?', t).fetchone()
    conn.close()
    return result


def search_artists(search=None):
    conn = sqlite3.connect(os.getenv('DB_PATH'))
    c = conn.cursor()
    query = """
        SELECT
          a.spotify_id, a.name
        FROM artist AS a
        WHERE
          (?1 IS NULL OR a.name LIKE ?1 || '%')
    """
    result = c.execute(query, (search,)).fetchall()
    conn.close()
    return result
