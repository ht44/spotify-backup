import os
import sys
import tkinter as tk
sys.path.insert(0, os.path.abspath('../../'))
from spotifybackup.interface.main import MainApplication

def do_nothing():
    print('nothing')
    pass


class Window(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent
        menubar = tk.Menu(parent)
        # create a pulldown menu, and add it to the menu bar
        filemenu = tk.Menu(menubar, tearoff=0)
        filemenu.add_command(label="Open", command=self.hello)
        filemenu.add_command(label="Save", command=self.hello)
        filemenu.add_separator()
        filemenu.add_command(label="Exit", command=self.hello)
        menubar.add_cascade(label="File", menu=filemenu)

        # create more pulldown menus
        editmenu = tk.Menu(menubar, tearoff=0)
        editmenu.add_command(label="Cut", command=self.hello)
        editmenu.add_command(label="Copy", command=self.hello)
        editmenu.add_command(label="Paste", command=self.hello)
        menubar.add_cascade(label="Edit", menu=editmenu)

        helpmenu = tk.Menu(menubar, tearoff=0)
        helpmenu.add_command(label="About", command=self.hello)
        menubar.add_cascade(label="Help", menu=helpmenu)

        parent.config(menu=menubar)

        app = MainApplication(parent)

    @staticmethod
    def hello():
        print('hello')

        # ctr_right.grid(row=0, column=2, sticky="ns")


if __name__ == "__main__":
    root = tk.Tk()
    root.title('Spotify Backup')
    root.geometry('{}x{}'.format(1500, 1000))
    Window(root)
    root.mainloop()

#
