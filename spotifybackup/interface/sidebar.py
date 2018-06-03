# Path hack.
import os
import sys
import tkinter as tk

from spotifybackup.database.album import get_albums
from spotifybackup.database.artist import get_artists
from spotifybackup.database.library import get_library
from spotifybackup.database.song import get_songs
from spotifybackup.spotify.backup import refresh, mock_fetch_library, refresh, fetch_library

class Sidebar(tk.Frame):
    def __init__(self, parent, controller, **kw):
        tk.Frame.__init__(self, parent, **kw)
        self.controller = controller
        library_button = tk.Button(
            parent,
            bg='#000000',
            fg='#b7f731',
            relief='flat',
            text='Library',
            anchor='w',
            width=20,
            command=lambda: controller.show_frame('LibraryTable')
            )

        songs_button = tk.Button(
            parent,
            bg='#000000',
            fg='#b7f731',
            relief='flat',
            text='Songs',
            anchor='w',
            width=20,
            command=lambda: controller.show_frame('SongTable')
            )

        albums_button = tk.Button(
            parent,
            bg='#000000',
            fg='#b7f731',
            relief='flat',
            text='Albums',
            anchor='w',
            width=20,
            command=lambda: controller.show_frame('AlbumTable')
            )

        artists_button = tk.Button(
            parent,
            bg='#000000',
            fg='#b7f731',
            relief='flat',
            text='Artists',
            anchor='w',
            width=20,
            command=lambda: controller.show_frame('ArtistTable')
            )

        backup_button = tk.Button(
            parent,
            bg='#000000',
            fg='#b7f731',
            relief='flat',
            text='Backup',
            anchor='w',
            width=20,
            command=self.backup
            )

        refresh_button = tk.Button(
            parent,
            bg='#000000',
            fg='#b7f731',
            relief='flat',
            text='Refresh',
            anchor='w',
            width=20,
            command=self.refresh
            )

        library_button.grid(row=0, sticky='W')
        songs_button.grid(row=1, sticky='W')
        albums_button.grid(row=2, sticky='W')
        artists_button.grid(row=3, sticky='W')
        refresh_button.grid(row=4, sticky=tk.W)
        backup_button.grid(row=5, sticky=tk.W)

    def backup(self):
        fetch_library()
        library = get_library()
        songs = get_songs()
        albums = get_albums()
        artists = get_artists()
        self.controller.frames['LibraryTable'].reload_table(library)
        self.controller.frames['SongsTable'].reload_table(songs)
        self.controller.frames['AlbumsTable'].reload_table(albums)
        self.controller.frames['ArtistsTable'].reload_table(artists)

    def refresh(self):
        refresh()