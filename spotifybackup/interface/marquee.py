import tkinter as tk
import tkinter.ttk as ttk

from spotifybackup.database.backup import get_last_backup


class Marquee(tk.Label):
    def __init__(self, parent, **kw):
        tk.Label.__init__(self, parent, **kw)
        # self.backup_text = tk.StringVar()
        # self.text = 'weeee'
        # self.config(text='weee', fg='white')
        self.last_backup = get_last_backup()
        self['fg'] = 'white'
        self['bg'] = 'blue'
        self.strvar = tk.StringVar()
        self.text = (
            '                    Last Backup: ' + str(self.last_backup[0]) + ''
            '                    Next Scheduled Backup: TBD'
        )
        self['textvariable'] = self.strvar
        self.should_stop = False
        self.animate()
        # self.pack(side='left', padx=(0, 40))
        # parent.backup_marquee.pack(side='left', padx=(0, 40))


        # self.backup_marquee = tk.Label(
        #     parent, textvariable=self.backup_text, fg='white', bg='black')
        #
        # last_backup = get_last_backup()
        #
        # if last_backup is None:
        #     text = 'No Backups'
        #     self.last_backup_label = tk.Label(parent, text=text, fg='white', bg='black')
        #     self.last_backup_label.pack(side='left', padx=(0, 40))
        # else:
        #     text = (
        #         '                    Last Backup: ' + str(last_backup[0]) + ''
        #         '                    Next Scheduled Backup: TBD'
        #     )

    # def marquee_animate_config(self):
    #     def marquee_animate():
    #         marquee_animate.text = marquee_animate.text[1:] + marquee_animate.text[0]
    #         strvar.set(marquee_animate.text)
    #         parent.after(delay, marquee_animate)
    #
    #     marquee_animate.text = text
    #     marquee_animate()
    #
    #
    # def marquee_animate(self):
    #     marquee_animate.text = marquee_animate.text[1:] + marquee_animate.text[0]
    #     strvar.set(marquee_animate.text)
    #     parent.after(delay, marquee_animate)
    def animate(self):
        if not self.should_stop:
            self.text = self.text[1:] + self.text[0]
            self.strvar.set(self.text)
            self.after(100, self.animate)

    def update_text(self):
        self.text = 'wee'