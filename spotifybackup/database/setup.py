import os
import sqlite3


def setup():
    conn = sqlite3.connect(os.getenv('DB_PATH'))
    c = conn.cursor()

    c.execute('''
        CREATE TABLE IF NOT EXISTS song (
          id INTEGER PRIMARY KEY,
          spotify_id TEXT NOT NULL UNIQUE,
          name TEXT NOT NULL,
          spotify_added_at TEXT DEFAULT NULL,
          album_id INTEGER NOT NULL,
          FOREIGN KEY(album_id) REFERENCES album(id)
        );''')

    c.execute('''CREATE TABLE IF NOT EXISTS artist (
          id INTEGER PRIMARY KEY,
          spotify_id TEXT NOT NULL UNIQUE,
          name TEXT NOT NULL
        );''')

    c.execute('''
        CREATE TABLE IF NOT EXISTS album (
          id INTEGER PRIMARY KEY,
          spotify_id TEXT NOT NULL UNIQUE,
          name TEXT NOT NULL
        );''')

    c.execute('''
        CREATE TABLE IF NOT EXISTS song_artist (
          id INTEGER PRIMARY KEY,
          song_id INTEGER NOT NULL,
          artist_id INTEGER NOT NULL,
          FOREIGN KEY(song_id) REFERENCES song(id),
          FOREIGN KEY(artist_id) REFERENCES artist(id)
        );''')

    c.execute('''
        CREATE TABLE IF NOT EXISTS album_artist (
          id INTEGER PRIMARY KEY,
          album_id INTEGER NOT NULL,
          artist_id INTEGER NOT NULL,
          FOREIGN KEY(album_id) REFERENCES album(id),
          FOREIGN KEY(artist_id) REFERENCES artist(id)
        );''')

    conn.commit()
    conn.close()
