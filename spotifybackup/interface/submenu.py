import tkinter as tk

# Path hack.
import sys, os

from spotifybackup.database.album import search_albums, count_albums
from spotifybackup.database.artist import search_artists, count_artists
from spotifybackup.database.backup import get_last_backup
from spotifybackup.database.song import search_songs, count_songs
from spotifybackup.database.library import search_all


class Submenu(tk.Frame):
    def __init__(self, parent, controller, **kw):
        tk.Frame.__init__(self, parent, **kw)
        self.controller = controller

        self.search_bar_label = tk.Label(
            parent, text='SEARCH: ',
            bg='#000000',
            fg='#b7f731'
            )

        self.search_bar = tk.Entry(parent, bg='white')
        self.search_bar.bind("<Key>", self.search)
        self.search_bar.pack(side='right')
        self.search_bar_label.pack(side='right')


        song_count = count_songs()
        text = 'Songs: ' + str(song_count[0])
        self.song_count_label = tk.Label(parent, text=text, fg='white', bg='black')
        self.song_count_label.pack(side='left', padx=(0, 40))

        album_count = count_albums()
        text = 'Albums: ' + str(album_count[0])
        self.album_count_label = tk.Label(parent, text=text, fg='white', bg='black')
        self.album_count_label.pack(side='left', padx=(0, 40))

        artist_count = count_artists()
        text = 'Artists: ' + str(artist_count[0])
        self.artist_count_label = tk.Label(parent, text=text, fg='white', bg='black')
        self.artist_count_label.pack(side='left', padx=(0, 40))

        deli = 100  # milliseconds of delay per character
        svar = tk.StringVar()
        labl = tk.Label(parent, textvariable=svar, fg='white', bg='black')

        def shif():
            shif.msg = shif.msg[1:] + shif.msg[0]
            svar.set(shif.msg)
            parent.after(deli, shif)

        last_backup = get_last_backup()

        if last_backup is None:
            text = 'No Backups'
            self.last_backup_label = tk.Label(parent, text=text, fg='white', bg='black')
            self.last_backup_label.pack(side='left', padx=(0, 40))
        else:
            text = (
                '                    Last Backup: ' + str(last_backup[0]) + ''
                '                    Next Scheduled Backup: TBD'
            )
            shif.msg = text
            shif()
            labl.pack(side='left', padx=(0, 40))

        # album_count = count_albums()
        # text = 'Albums: ' + album_count
        # self.album_count_label = tk.Label(parent, text=text)
        # self.album_count_label.pack(side='left')
        #
        # artist_count = count_artists()
        # text = 'Artists: ' + artist_count
        # self.artist_count_label = tk.Label(parent, text=text)
        # self.artist_count_label.pack(side='left')

    def search(self, e=None):
        text = self.search_bar.get()
        active_frame_name = self.controller.notebook.notebook.tab(self.controller.notebook.notebook.select(), "text")
        func = search_all
        if active_frame_name == 'Library':
            func = search_all
            view = self.controller.notebook.library
        elif active_frame_name == 'Songs':
            func = search_songs
            view = self.controller.notebook.songs
        elif active_frame_name == 'Albums':
            func = search_albums
            view = self.controller.notebook.albums
        elif active_frame_name == 'Artists':
            func = search_artists
            view = self.controller.notebook.artists
        #
        records = func(search=text)
        view.reload_table(records)