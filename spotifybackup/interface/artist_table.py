import tkinter as tk
import tkinter.ttk as ttk

# Path hack.
import sys, os
sys.path.insert(0, os.path.abspath('../../'))
from spotifybackup.database.artist import get_artists


class ArtistTable(tk.Frame):
    def __init__(self, parent, controller, **kw):
        tk.Frame.__init__(self, parent, **kw)
        self.grid(sticky=('N', 'S', 'W', 'E'))
        parent.grid_rowconfigure(0, weight=1)
        parent.grid_columnconfigure(0, weight=1)
        s = ttk.Style()
        s.configure('Treeview', rowheight=45)

        tree = ttk.Treeview(self)
        tree['show'] = 'headings'
        tree.tag_configure('even', background='white')
        tree.tag_configure('odd', background='#dddddd')
        tree['columns'] = ('spotify_id', 'name',)
        for each in tree['columns']:
            tree.heading(each,
                         text=each.capitalize(),
                         command=lambda each_=each: self.treeview_sort_column(tree, each_, False))
        tree.heading('spotify_id', text='Spotify ID')
        tree.column('spotify_id', anchor='w', width=100)
        tree.heading('name', text='Name')
        tree.column('name', anchor='w', width=100)
        tree.grid(sticky=('N', 'S', 'W', 'E'))
        self.treeview = tree
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)
        self.load_table()

    def treeview_sort_column(self, tv, col, reverse):
        l = [(tv.set(k, col), k) for k in tv.get_children('')]
        l.sort(reverse=reverse)

        # rearrange items in sorted positions
        for index, (val, k) in enumerate(l):
            tv.move(k, '', index)
            if index % 2 == 0:
                tv.item(k, tags=('even',))
            else:
                tv.item(k, tags=('odd',))

        # reverse sort next time
        tv.heading(col, command=lambda: self.treeview_sort_column(tv, col, not reverse))

    def load_table(self):
        records = get_artists()
        for r in list(enumerate(records)):
            if r[0] % 2 == 0:
                rowmod = 'even'
            else:
                rowmod = 'odd'
            self.treeview.insert(
                '', 'end', text=r[0], values=(r[1][0], r[1][1]), tags=(rowmod,))

    def reload_table(self, records):
        self.treeview.delete(*self.treeview.get_children())
        for r in list(enumerate(records)):
            if r[0] % 2 == 0:
                rowmod = 'even'
            else:
                rowmod = 'odd'
            self.treeview.insert(
                '', 'end', text=r[0], values=(r[1][0], r[1][1]), tags=(rowmod,))

