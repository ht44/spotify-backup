import os
from base64 import b64encode
from pprint import pprint
from .constants import TOKEN_ENDPOINT
import requests
import json
import spotifybackup.database.library as library

# with open('library.json', 'w') as outfile:
#     json.dump(result, outfile)


def refresh():
    creds = bytes(os.getenv('CLIENT_ID') + ':' + os.getenv('CLIENT_SECRET'), encoding='utf-8')
    b64creds = b64encode(creds).decode('ascii')
    headers = {'Authorization': 'Basic %s' % b64creds}
    payload = {
        'grant_type': 'refresh_token',
        'refresh_token': os.getenv('REFRESH_TOKEN'),
    }
    r = requests.post(TOKEN_ENDPOINT, data=payload, headers=headers)
    j = r.json()
    if 'error' in j:
        print(j['error'])
    os.environ['ACCESS_TOKEN'] = j['access_token']
    print(j)


def mock_fetch_library():
    with open('library.json') as data_file:
        result = json.load(data_file)
        result = [SpotifyTrack(t) for t in result]
        lib = SpotifyLibrary(result)
        library.insert(
            lib.songs_tuple,
            lib.unique_albums_tuple,
            lib.unique_artists_tuple,
            lib.song_artist_tuples)


def fetch_library():
    auth_header = 'Authorization: Bearer {}'.format(os.getenv('ACCESS_TOKEN'))
    headers = {'Authorization': auth_header}
    r = requests.get('https://api.spotify.com/v1/me/tracks?limit=50', headers=headers)
    j = r.json()
    if 'error' in j:
        print(j['error'])
    result = j['items']
    while j['next']:
        r = requests.get(j['next'], headers=headers)
        j = r.json()
        if 'error' in j:
            print(j['error'])
        result = result + j['items']

    result = [SpotifyTrack(t) for t in result]
    lib = SpotifyLibrary(result)
    pprint(lib.songs)
    library.insert(
        lib.songs_tuple,
        lib.unique_albums_tuple,
        lib.unique_artists_tuple,
        lib.song_artist_tuples)


class SpotifyLibrary:
    def __init__(self, tracks):
        self.songs = [t.__dict__ for t in tracks]
        albums = [s['album'] for s in self.songs]
        artists = [s['artists'] for s in self.songs]
        flat_artists = [item for sublist in artists for item in sublist]
        unique_artists = list({a['spotify_id']: a for a in flat_artists}.values())
        unique_albums = list({a['spotify_id']: a for a in albums}.values())
        self.unique_albums_tuple = [(a['spotify_id'], a['name']) for a in unique_albums]
        self.unique_artists_tuple = [(a['spotify_id'], a['name']) for a in unique_artists]
        self.songs_tuple = [
            (s['spotify_id'], s['name'], s['spotify_added_at'], s['album']['spotify_id'])
            for s in self.songs
        ]

        self.song_artist_tuples = [i for i in self.clean_song_artist()]

    def clean_song_artist(self):
        for s in self.songs:
            song_spotify_id = s['spotify_id']
            for a in s['artists']:
                artist_spotify_id = a['spotify_id']
                yield ((song_spotify_id, artist_spotify_id))


class SpotifyTrack:
    def __init__(self, track):
        self.spotify_id = track['track']['id']
        self.spotify_added_at = track['added_at']
        self.name = track['track']['name']
        self.artists = [{'spotify_id': a['id'], 'name': a['name']} for a in track['track']['artists']]
        self.album = {
            'spotify_id': track['track']['album']['id'],
            'name': track['track']['album']['name']
        }
