from tkinter import Label, Entry
from buttons import TextButton
import tkinter as tk
import re


class AddWindow(tk.Toplevel):
    def __init__(self, master, data):
        super().__init__(master=master)

        self['width'] = 300
        self['height'] = 200
        self['bg'] = master['bg']
        self.geometry(f'{self['width']}x{self['height']}+830+450')
        self.resizable(width=False,
                       height=False)

        self.data = data

        self.name_label = Label(master=self,
                                text='Name:',
                                font=(self.data.font, 12),
                                bg=self['bg'])
        self.name_label.place(x=self['width'] * 0.07,
                              y=self['height'] * 0.1)

        name_entry = Entry(master=self,
                           borderwidth=0,
                           justify='center',
                           width=27)
        name_entry.place(x=self['width'] * 0.42,
                         y=self['height'] * 0.1)

        email_label = Label(master=self,
                            text='Email:',
                            font=(self.data.font, 12),
                            bg=self['bg'])
        email_label.place(x=self['width'] * 0.07,
                          y=self['height'] * 0.325)

        email_entry = Entry(master=self,
                            borderwidth=0,
                            justify='center',
                            width=27)
        email_entry.place(x=self['width'] * 0.42,
                          y=self['height'] * 0.325)

        birthday_date_label = Label(master=self,
                                    text='Birthday date:',
                                    font=(self.data.font, 12),
                                    bg=self['bg'])
        birthday_date_label.place(x=self['width'] * 0.07,
                                  y=self['height'] * 0.55)

        birthday_date_entry = Entry(master=self,
                                    borderwidth=0,
                                    justify='center',
                                    width=27)
        birthday_date_entry.place(x=self['width'] * 0.42,
                                  y=self['height'] * 0.56)

        self.error_message = Label(master=self, text='',
                                   font=(self.data.font, 12),
                                   bg=self['bg'], fg='red')
        self.error_message.place(x=self['width'] * 0.1,
                                 y=self['height'] * 0.67)

        cancel_btn = TextButton(master=self,
                                text='Cancel',
                                size=14,
                                command=self._destroy)
        cancel_btn.place(x=self['width'] * 0.15,
                         y=self['height'] * 0.8)

        save_btn = TextButton(master=self,
                              text='Save',
                              size=14,
                              command=lambda: self._validate_entry(name_entry.get(), email_entry.get(),
                                                                   birthday_date_entry.get()))
        save_btn.place(x=self['width'] * 0.65,
                       y=self['height'] * 0.8)

        self.bind('<Return>',
                  lambda _e: self._validate_entry(name_entry.get(), email_entry.get(), birthday_date_entry.get()))
        self.focus()

    def _destroy(self):
        self.master.erase_binding()
        self.destroy()

    def _validate_entry(self, name, email, date):
        name_format = r'\b[A-Za-z]{2,15} [A-Za-z]{2,15}\b'
        mail_format = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
        date_format = r'\b[0-9]{2}+-[0-9]{2}+-[0-9]{4}\b'

        if re.fullmatch(name_format, name) and re.fullmatch(mail_format, email) and re.fullmatch(date_format, date):
            self.data.data_file.loc[len(self.data.data_file)] = [name, email, date, [],'N']
            self.data.update_file()
            self.master.update_table()
            self._destroy()
        else:
            self.error_message.config(text='one or more fields are incorrectly filled')
