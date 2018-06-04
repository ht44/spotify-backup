import os
import sqlite3


def get_songs():
    conn = sqlite3.connect(os.getenv('DB_PATH'))
    c = conn.cursor()
    result = c.execute('''SELECT spotify_id, name, spotify_added_at FROM song''').fetchall()
    conn.close()
    return result


def get_song(song_id):
    conn = sqlite3.connect(os.getenv('DB_PATH'))
    c = conn.cursor()
    t = (song_id,)
    result = c.execute('SELECT * FROM song WHERE id=?', t).fetchone()
    conn.close()
    return result


def count_songs():
    conn = sqlite3.connect(os.getenv('DB_PATH'))
    c = conn.cursor()
    result = c.execute('SELECT COUNT(*) FROM song').fetchone()
    conn.close()
    return result


def search_songs(search=None):
    conn = sqlite3.connect(os.getenv('DB_PATH'))
    c = conn.cursor()
    query = """
        SELECT
          s.spotify_id, s.name, s.spotify_added_at
        FROM song AS s
        WHERE
          (?1 IS NULL OR s.name LIKE ?1 || '%')
    """
    result = c.execute(query, (search,)).fetchall()
    conn.close()
    return result
