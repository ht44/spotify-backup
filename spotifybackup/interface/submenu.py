import tkinter as tk

# Path hack.
import sys, os

from spotifybackup.database.album import search_albums
from spotifybackup.database.artist import search_artists
from spotifybackup.database.song import search_songs

sys.path.insert(0, os.path.abspath('../../'))
from spotifybackup.database.library import search_all

class Submenu(tk.Frame):
    def __init__(self, parent, controller, **kw):
        tk.Frame.__init__(self, parent, **kw)
        self.controller = controller
        self.search_bar = tk.Entry(parent, bg='white')
        self.search_bar.bind("<Key>", self.search)

        self.search_bar.pack(side='right')

        self.search_button = tk.Button(
            parent,
            bg='#000000',
            fg='#b7f731',
            relief='flat',
            text='Search',
            command=self.search
            )
        self.search_button.pack(side='right')

    def search(self, e=None):
        text = self.search_bar.get()
        active_frame_name = self.controller.active_frame_name

        func = search_all
        if active_frame_name == 'LibraryTable':
            func = search_all
        elif active_frame_name == 'SongTable':
            func = search_songs
        elif active_frame_name == 'AlbumTable':
            func = search_albums
        elif active_frame_name == 'ArtistTable':
            func = search_artists

        records = func(search=text)
        view = self.controller.frames[active_frame_name]
        view.reload_table(records)