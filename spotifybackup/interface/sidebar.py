# Path hack.
import os
import sys
import tkinter as tk

sys.path.insert(0, os.path.abspath('../../'))


class Sidebar(tk.Frame):
    def __init__(self, parent, controller, **kw):
        tk.Frame.__init__(self, parent, **kw)

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

        library_button.grid(row=0, sticky='W')
        songs_button.grid(row=1, sticky='W')
        albums_button.grid(row=2, sticky='W')
        artists_button.grid(row=3, sticky='W')
