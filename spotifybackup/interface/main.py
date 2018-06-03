import os
import sys
import tkinter as tk
sys.path.insert(0, os.path.abspath('../../'))
from spotifybackup.interface.table import LibraryTable




class MainApplication(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent
        top_frame = tk.Frame(parent, bg='cyan', width=450, height=50, pady=3)
        center = tk.Frame(parent, bg='gray2', width=50, height=40, padx=3, pady=3)

        # layout all of the main containers
        parent.grid_rowconfigure(1, weight=1)
        parent.grid_columnconfigure(0, weight=1)

        top_frame.grid(row=0, sticky="ew")
        center.grid(row=1, sticky="nsew")

        # create the widgets for the top frame
        song_label = tk.Label(top_frame, text='Song:')
        album_label = tk.Label(top_frame, text='Album:')
        artist_label = tk.Label(top_frame, text='Artist:')

        entry_song = tk.Entry(top_frame, background="white")
        entry_album = tk.Entry(top_frame, background="white")
        entry_artist = tk.Entry(top_frame, background="white")

        # layout the widgets in the top frame
        song_label.grid(row=0, column=0)
        album_label.grid(row=0, column=1)
        artist_label.grid(row=0, column=2)

        entry_song.grid(row=1, column=0)
        entry_album.grid(row=1, column=1)
        entry_artist.grid(row=1, column=2)

        # create the center widgets
        center.grid_rowconfigure(0, weight=1)
        center.grid_columnconfigure(1, weight=1)

        ctr_left = tk.Frame(center, bg='green', width=200, height=300)
        ctr_mid = tk.Frame(center, bg='grey', width=250, height=300, padx=3, pady=3)
        ctr_mid.library_table = LibraryTable(ctr_mid)

        # self.library.grid(row=0, column=0)
        # ctr_right = Frame(center, bg='green', width=100, height=300, padx=3, pady=3)

        ctr_left.grid(row=0, column=0, sticky="ns")
        ctr_mid.grid(row=0, column=1, sticky="nsew")
        # ctr_right.grid(row=0, column=2, sticky="ns")

#
#
# root = Tk()
# root.title('Spotify Backup')
# root.geometry('{}x{}'.format(500, 500))

# create all of the main containers

#
# app = Window(root)
# root.mainloop()


if __name__ == "__main__":
    root = tk.Tk()
    root.title('Spotify Backup')
    root.geometry('{}x{}'.format(1500, 1000))
    MainApplication(root)
    root.mainloop()
