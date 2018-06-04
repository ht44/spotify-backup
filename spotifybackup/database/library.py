import os
import sqlite3


def get_library():
    conn = sqlite3.connect(os.getenv('DB_PATH'))
    c = conn.cursor()
    result = c.execute('''
        SELECT
          s.spotify_added_at as added_at,
          s.name AS song,
          al.name as album,
          GROUP_CONCAT(a.name, ', ') AS artist
        FROM song AS s
          JOIN album AS al
            ON s.album_id = al.id
          LEFT JOIN song_artist AS sa
            ON sa.song_id = s.id
          LEFT JOIN artist AS a
            ON a.id = sa.artist_id
        GROUP BY s.name
        ORDER BY s.spotify_added_at DESC;
      ''').fetchall()
    conn.close()
    return result


def search_library(song=None, album=None, artist=None):
    conn = sqlite3.connect(os.getenv('DB_PATH'))
    c = conn.cursor()
    query = """

        SELECT
          s.spotify_added_at as added_at,
          s.name AS song,
          al.name as album,
          GROUP_CONCAT(a.name, ', ') AS artist
        FROM song AS s
          JOIN album AS al
            ON s.album_id = al.id
          LEFT JOIN song_artist AS sa
            ON sa.song_id = s.id
          LEFT JOIN artist AS a
            ON a.id = sa.artist_id
        GROUP BY s.name
        HAVING
          (?1 IS NULL OR s.name LIKE ?1 || '%')
          OR
          (?2 IS NULL OR al.name LIKE ?2 || '%')
          OR 
          (?3 IS NULL OR  artist like ?3 || '%')
    """
    result = c.execute(query, (song, album, artist)).fetchall()
    conn.close()
    return result


def search_all(search=None):
    conn = sqlite3.connect(os.getenv('DB_PATH'))
    c = conn.cursor()
    query = """

        SELECT
          s.spotify_added_at as added_at,
          s.name AS song,
          al.name as album,
          GROUP_CONCAT(a.name, ', ') AS artist
        FROM song AS s
          JOIN album AS al
            ON s.album_id = al.id
          LEFT JOIN song_artist AS sa
            ON sa.song_id = s.id
          LEFT JOIN artist AS a
            ON a.id = sa.artist_id
        GROUP BY s.name
        HAVING
          (?1 IS NULL OR s.name LIKE ?1 || '%')
          OR
          (?1 IS NULL OR al.name LIKE ?1 || '%')
          OR 
          (?1 IS NULL OR  artist like ?1 || '%')
    """
    result = c.execute(query, (search,)).fetchall()
    conn.close()
    return result


def insert(song_tuples, album_tuples, artist_tuples, song_artist_tuples):
    conn = sqlite3.connect(os.getenv('DB_PATH'))
    c = conn.cursor()

    c.executemany('''
        INSERT OR IGNORE INTO artist (spotify_id, name) VALUES (?, ?)
        ''', artist_tuples)

    c.executemany('''
        INSERT OR IGNORE INTO album (spotify_id, name) VALUES (?, ?)
        ''', album_tuples)

    c.executemany('''
        INSERT OR IGNORE INTO
          song (spotify_id, name, spotify_added_at, album_id)
        VALUES (?, ?, ?, (SELECT id from album where ? = album.spotify_id))
        ''', song_tuples)

    c.executemany('''
        INSERT OR IGNORE INTO
          song_artist (song_id, artist_id)
        VALUES (
          (SELECT id from song where ? = song.spotify_id),
          (SELECT id from artist where ? = artist.spotify_id)
        )
        ''', song_artist_tuples)
    conn.commit()
    conn.close()
