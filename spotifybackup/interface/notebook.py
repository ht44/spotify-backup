import tkinter as tk
from tkinter import ttk

from spotifybackup.interface.album_table import AlbumTable
from spotifybackup.interface.artist_table import ArtistTable
from spotifybackup.interface.library_table import LibraryTable
from spotifybackup.interface.song_table import SongTable


class Notebook(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)

        self.notebook = ttk.Notebook(parent)

        self.library = LibraryTable(parent, controller=None)
        self.songs = SongTable(parent, controller=None)
        self.albums = AlbumTable(parent, controller=None)
        self.artists = ArtistTable(parent, controller=None)
        self.notebook.add(self.library, text="Library")
        self.notebook.add(self.songs, text="Songs")
        self.notebook.add(self.albums, text="Albums")
        self.notebook.add(self.artists, text="Artists")

        self.notebook.pack(fill='both', expand=True)