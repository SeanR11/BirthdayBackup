import tkinter as tk


class TextButton(tk.Button):
    def __init__(self, master, text, command=print, size=30):
        super().__init__(master=master,
                         text=text,
                         borderwidth=0,
                         anchor='center',
                         command=command)

        self['bg'] = self.master['bg']
        self['font'] = ('David', size)
        self['activebackground'] = self.master['bg']


class ImageButton(tk.Button):
    def __init__(self, master, image, command=print):
        super().__init__(master=master,
                         image=image,
                         borderwidth=0,
                         anchor='center',
                         command=command)
        self['bg'] = self.master['bg']
        self['activebackground'] = self.master['bg']
