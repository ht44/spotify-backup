from . import backup, constants
from os import environ, getenv
from spotifybackup.env import CLIENT_ID, CLIENT_SECRET, REFRESH_TOKEN, DB_PATH

environ['CLIENT_ID'] = CLIENT_ID
environ['CLIENT_SECRET'] = CLIENT_SECRET
environ['REFRESH_TOKEN'] = REFRESH_TOKEN
environ['DB_PATH'] = DB_PATH


def checkenv():
    print(getenv('CLIENT_ID'))
    print(getenv('CLIENT_SECRET'))
    print(getenv('REFRESH_TOKEN'))
    print(getenv('ACCESS_TOKEN'))
    print(getenv('DB_PATH'))