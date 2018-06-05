import tkinter as tk

# Path hack.
import sys, os

from spotifybackup.database.album import search_albums, count_albums
from spotifybackup.database.artist import search_artists, count_artists
from spotifybackup.database.backup import get_last_backup
from spotifybackup.database.song import search_songs, count_songs
from spotifybackup.database.library import search_all
from spotifybackup.interface.marquee import Marquee


class Submenu(tk.Frame):
    def __init__(self, parent, controller, **kw):
        tk.Frame.__init__(self, parent, **kw)
        self.parent = parent
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


        self.backup_text = tk.StringVar()

        self.backup_marquee = tk.Label(
            parent, textvariable=self.backup_text, fg='white', bg='black')

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
            # shif.msg = text
            # self.marquee_animate_config(text, parent, self.backup_text, 100)
            # marquee_animate.msg = text
            # marquee_animate(self.backup_text, parent, 100)
            # self.backup_marquee.pack(side='left', padx=(0, 40))

            self.marquee = Marquee(parent)
            self.marquee.pack(side='left', padx=(0, 40))
        # album_count = count_albums()
        # text = 'Albums: ' + album_count
        # self.album_count_label = tk.Label(parent, text=text)
        # self.album_count_label.pack(side='left')
        #
        # artist_count = count_artists()
        # text = 'Artists: ' + artist_count
        # self.artist_count_label = tk.Label(parent, text=text)
        # self.artist_count_label.pack(side='left')

    def marquee_animate_config(self, text, parent, strvar, delay):
        def marquee_animate():
            marquee_animate.text = marquee_animate.text[1:] + marquee_animate.text[0]
            strvar.set(marquee_animate.text)
            parent.after(delay, marquee_animate)

        marquee_animate.text = text
        marquee_animate()


    def update_backup_text(self, last_backup):
        text = (
            '                    LAST Backup: ' + last_backup + ''
            '                    Next Scheduled Backup: TBD'
        )
        self.backup_text.set(text)
        self.backup_marquee['text'] = text
        self.backup_marquee.destroy()
        self.backup_marquee = tk.Label(
            self.parent, textvariable=self.backup_text, fg='white', bg='black')
        self.marquee_animate_config(text, self.parent, self.backup_text, 100)
        self.backup_marquee.pack(side='left', padx=(0, 40))


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


    def animate(self):
        if not self.should_stop:
            self.draw_one_frame()
            self.after(100, self.animate)