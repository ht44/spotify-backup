import tkinter as tk
from spotifybackup.database.album import get_albums, count_albums
from spotifybackup.database.artist import get_artists, count_artists
from spotifybackup.database.backup import insert_backup, get_last_backup
from spotifybackup.database.library import get_library
from spotifybackup.database.song import get_songs, count_songs
from spotifybackup.spotify.backup import mock_fetch_library, refresh, fetch_library


class Sidebar(tk.Frame):
    def __init__(self, parent, controller, **kw):
        tk.Frame.__init__(self, parent, **kw)
        self.controller = controller

        backup_button = tk.Button(
            parent,
            bg='#000000',
            fg='#b7f731',
            activebackground='green',
            activeforeground='white',
            bd=0,
            cursor='heart',
            relief='flat',
            text='Backup',
            anchor='w',
            width=10,
            command=self.backup
            )

        refresh_button = tk.Button(
            parent,
            bg='#000000',
            fg='#b7f731',
            activebackground='green',
            activeforeground='white',
            bd=0,
            cursor='heart',
            relief='flat',
            text='Refresh',
            anchor='w',
            width=10,
            command=self.refresh
            )

        # library_button.grid(row=0, sticky='W')
        # songs_button.grid(row=1, sticky='W')
        # albums_button.grid(row=2, sticky='W')
        # artists_button.grid(row=3, sticky='W')
        # refresh_button.grid(row=4, sticky=tk.W)
        # backup_button.grid(row=5, sticky=tk.S)

        refresh_button.pack(side='top')
        backup_button.pack(side='top')

    def backup(self):
        # fetch_library()
        # insert_backup()
        # library = get_library()
        # songs = get_songs()
        # albums = get_albums()
        # artists = get_artists()
        # song_count = count_songs()
        # album_count = count_albums()
        # artist_count = count_artists()
        last_backup = get_last_backup()

        # self.controller.submenu.song_count_label['text'] = 'Songs: ' + str(song_count[0])
        # self.controller.submenu.album_count_label['text'] = 'Albums: ' + str(album_count[0])
        # self.controller.submenu.artist_count_label['text'] = 'Artists: ' + str(artist_count[0])
        # self.controller.notebook.library.reload_table(library)
        # self.controller.notebook.songs.reload_table(songs)
        # self.controller.notebook.albums.reload_table(albums)
        # self.controller.notebook.artists.reload_table(artists)
        self.controller.submenu.marquee.text = 'weee'

    @staticmethod
    def refresh():
        refresh()