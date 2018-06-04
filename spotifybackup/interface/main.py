import tkinter as tk
from spotifybackup.interface.album_table import AlbumTable
from spotifybackup.interface.artist_table import ArtistTable
from spotifybackup.interface.notebook import Notebook
from spotifybackup.interface.song_table import SongTable
from spotifybackup.interface.library_table import LibraryTable
from spotifybackup.interface.sidebar import Sidebar
from spotifybackup.interface.submenu import Submenu


def do_nothing():
    print('nothing')
    pass


class MainApplication(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent
        top_frame = tk.Frame(parent, bg='gray3', width=450, height=50)
        center = tk.Frame(parent, bg='gray2', width=50, height=40)

        # layout all of the main containers
        parent.grid_rowconfigure(1, weight=1)
        parent.grid_columnconfigure(0, weight=1)

        top_frame.grid(row=0, sticky="ew")
        center.grid(row=1, sticky="nsew")

        center.grid_rowconfigure(0, weight=1)
        center.grid_columnconfigure(1, weight=1)

        main_frame = tk.Frame(center, bg='grey', width=250, height=300, padx=3, pady=3)

        sidebar_frame = tk.Frame(center, bg='#032625', width=200, height=300)

        sidebar_frame.grid(row=0, column=0, sticky="ns")
        main_frame.grid(row=0, column=1, sticky="nsew")

        self.notebook = Notebook(main_frame)
        self.submenu = Submenu(parent=top_frame, controller=self)
        self.sidebar = Sidebar(parent=sidebar_frame, controller=self)


        # ctr_right.grid(row=0, column=2, sticky="ns")

        # self.frames = {}
        # for F in (LibraryTable, ArtistTable, AlbumTable, SongTable):
        #     page_name = F.__name__
        #     frame = F(parent=main_frame, controller=self)
        #     self.frames[page_name] = frame
        #     # put all of the pages in the same location;
        #     # the one on the top of the stacking order
        #     # will be the one that is visible.
        #     frame.grid(row=0, column=0, sticky="nsew")

        # self.show_frame("LibraryTable")
        # self.active_frame_name = 'LibraryTable'


        # hayden.pack(side='left', expand=True)

    def show_frame(self, page_name):
        self.active_frame_name = page_name
        frame = self.frames[page_name]
        frame.tkraise()