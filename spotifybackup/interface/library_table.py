import tkinter as tk
import tkinter.ttk as ttk

# Path hack.
import sys, os
sys.path.insert(0, os.path.abspath('../../'))
from spotifybackup.database.library import get_library


class LibraryTable(tk.Frame):
    def __init__(self, parent, controller, **kw):
        tk.Frame.__init__(self, parent, **kw)
        self.grid(sticky=('N', 'S', 'W', 'E'))
        parent.grid_rowconfigure(0, weight=1)
        parent.grid_columnconfigure(0, weight=1)
        s = ttk.Style()
        s.configure('Treeview', rowheight=45)

        # scrollbarx = tk.Scrollbar(parent, orient=tk.HORIZONTAL)
        # scrollbary = tk.Scrollbar(parent, orient=tk.VERTICAL)

        tree = ttk.Treeview(self)
        #
        # scrollbary.config(command=tree.yview)
        # scrollbary.pack(side=tk.RIGHT, fill=tk.Y)
        # scrollbarx.config(command=tree.xview)
        # scrollbarx.pack(side=tk.BOTTOM, fill=tk.X)

        tree['show'] = 'headings'
        tree.tag_configure('even', background='white')
        tree.tag_configure('odd', background='#dddddd')
        tree['columns'] = ('song', 'album', 'artist', 'added_at')
        for each in ('song', 'album', 'artist', 'added_at'):
            tree.heading(each,
                         text=each.capitalize(),
                         command=lambda each_=each: self.treeview_sort_column(tree, each_, False))
        tree.heading('song', text='Song')
        tree.column('song', anchor='w', width=100)
        tree.heading('album', text='Album')
        tree.column('album', anchor='w', width=100)
        tree.heading('artist', text='Artist')
        tree.column('artist', anchor='w', width=100)
        tree.heading('added_at', text='Added At')
        tree.column('added_at', anchor='w', width=100)
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
        records = get_library()
        for r in list(enumerate(records)):
            if r[0] % 2 == 0:
                rowmod = 'even'
            else:
                rowmod = 'odd'
            self.treeview.insert(
                '', 'end', text=r[0], values=(r[1][1], r[1][2], r[1][3], r[1][0]), tags=(rowmod,))

    def reload_table(self, records):
        self.treeview.delete(*self.treeview.get_children())
        for r in list(enumerate(records)):
            if r[0] % 2 == 0:
                rowmod = 'even'
            else:
                rowmod = 'odd'
            self.treeview.insert(
                '', 'end', text=r[0], values=(r[1][1], r[1][2], r[1][3], r[1][0]), tags=(rowmod,))