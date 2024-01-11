from tkinter import Label, Entry
from buttons import TextButton
import tkinter as tk
import re


class SearchWindow(tk.Toplevel):
    def __init__(self, master, data):
        super().__init__(master=master)

        self['width'] = 300
        self['height'] = 200
        self['bg'] = master['bg']
        self.geometry(f'{self['width']}x{self['height']}+830+450')
        self.resizable(width=False,
                       height=False)

        self.data = data

        self.search_label = Label(master=self,
                                  text='Enter name:',
                                  font=(self.data.font, 16),
                                  borderwidth=0, bg=self['bg'])
        self.search_label.pack(pady=30)

        self.search_entry = Entry(master=self,
                                  highlightthickness=0,
                                  bg='white',
                                  justify='center')
        self.search_entry.pack()

        self.search_btn = TextButton(master=self,
                                     text='search',
                                     size=12,
                                     command=self._search_item)
        self.search_btn.pack(pady=30)

        self.error_message = Label(master=self,
                                   text='',
                                   font=(self.data.font, 14),
                                   bg=self['bg'],
                                   fg='red')
        self.error_message.pack()

        self.bind('<Return>',
                  lambda _e: self._search_item())
        self.focus()

    def _destroy(self):
        self.master.erase_binding()
        self.destroy()

    def _search_item(self):
        search_key = self.search_entry.get()
        if search_key.lower() in self.data.data_file['Name'].tolist():
            for widget in self.winfo_children():
                widget.destroy()

            data = self.data.data_file.loc[self.data.data_file.index[self.data.data_file['Name'] == search_key.lower()]]
            name_label = Label(master=self,
                               text='Name',
                               font=(self.data.font, 12)
                               , bg=self['bg'])
            name_label.place(x=self['width'] * 0.1,
                             y=self['height'] * 0.2)

            name_entry = Entry(master=self,
                               borderwidth=0,
                               justify='center')
            name_entry.insert(index=0,
                              string=data['Name'].tolist()[0])
            name_entry.place(x=self['width'] * 0.5,
                             y=self['height'] * 0.2)

            birthday_date_label = Label(master=self,
                                        text='Birthday date',
                                        font=(self.data.font, 12),
                                        bg=self['bg'])
            birthday_date_label.place(x=self['width'] * 0.1,
                                      y=self['height'] * 0.5)

            birthday_date_entry = Entry(master=self,
                                        borderwidth=0,
                                        justify='center')
            birthday_date_entry.insert(index=0,
                                       string=data['Birthday date'].tolist()[0])
            birthday_date_entry.place(x=self['width'] * 0.5,
                                      y=self['height'] * 0.5)

            cancel_btn = TextButton(master=self,
                                    text='Cancel',
                                    size=14,
                                    command=self._destroy)
            cancel_btn.place(x=self['width'] * 0.15,
                             y=self['height'] * 0.8)

            save_btn = TextButton(master=self,
                                  text='Save',
                                  size=14,
                                  command=lambda: self._save(search_key,
                                                             name_entry.get(),
                                                             birthday_date_entry.get()))
            save_btn.place(x=self['width'] * 0.65,
                           y=self['height'] * 0.8)
        else:
            self.error_message.config(text='Name does not exist in the list')

    def _save(self, key, name, date):
        date_format = r'\b[0-9]{2}+-[0-9]{2}+-[0-9]{4}\b'
        if re.fullmatch(date_format,date):
            data = self.data.data_file.loc[self.data.data_file.index[self.data.data_file['Name'] == key.lower()]].copy()
            data['Name'] = name
            data['Birthday date'] = date
            self.data.data_file.loc[self.data.data_file.index[self.data.data_file['Name'] == key.lower()]] = data

            self.data.update_file()
            self.master.update_table()
        self._destroy()
