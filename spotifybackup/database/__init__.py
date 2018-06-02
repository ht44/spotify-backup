from os import environ
from . import song, album, artist, library
from spotifybackup.env import DB_PATH

environ['DB_PATH'] = DB_PATH