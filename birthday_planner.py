from serach_window import SearchWindow
from add_window import AddWindow
from tkinter.ttk import Treeview
from buttons import ImageButton
from tkinter import Label,Frame
import tkinter as tk
import pandas as pd


class BirthdayPlanner(tk.Frame):

    def __init__(self, master, data):
        super().__init__(master=master)

        self['bg'] = self.master['bg']
        self['width'] = self.master.winfo_width()
        self['height'] = self.master.winfo_height()
        self.data = data

        self.header_frame = Frame(master=self,
                                  bg=master['bg'],
                                  width=self['width'],
                                  height=int(self['height'] * 0.1))
        self.header_frame.pack()

        self.return_btn = ImageButton(master=self.header_frame,
                                      image=self.data.buttons['return'],
                                      command=self.destroy)
        self.return_btn.place(x=10,
                              y=10)

        self.headline = Label(master=self.header_frame,
                              text='Plan Birthday Backups',
                              borderwidth=0,
                              bg=self.header_frame['bg'],
                              font=('david', 30))
        self.headline.place(x=self['width'] * 0.25,
                            y=10)

        self.trash_btn = ImageButton(master=self.header_frame,
                                     image=self.data.buttons['trash'],
                                     command=self._delete_item)
        self.trash_btn.place(x=self['width'] - 50,
                             y=10)

        self.search_btn = ImageButton(master=self.header_frame,
                                      image=self.data.buttons['search'],
                                      command=self._search_item)
        self.search_btn.place(x=self['width'] - 110,
                              y=10)

        self.add_btn = ImageButton(master=self.header_frame,
                                   image=self.data.buttons['add'],
                                   command=self._add_item)
        self.add_btn.place(x=self['width'] - 180,
                           y=10)

        self.main_frame = Frame(master=self, bg=master['bg'],
                                width=self['width'],
                                height=self['height'] * 0.9)
        self.main_frame.pack()

        self.columns = self.data.data_file.columns.tolist()
        self.table = Treeview(master=self.main_frame,
                              height=26)
        self.table['columns'] = self.columns
        self.table.column("#0",
                          width=0,
                          stretch=False)
        for col in self.table['columns']:
            self.table.heading(col,
                               text=col,
                               anchor='center')
            self.table.column(col, width=int(self['width'] / 5),
                              anchor='center')

        self.fill_table()
        self.table.pack()

        self.pack()

    def _delete_item(self):
        if self._check_window(SearchWindow) and self._check_window(AddWindow) and self.table.selection() != ():
            index = self.table.selection()[0]
            self.data.data_file = self.data.data_file.drop([int(index)])
            self.data.update_file()
            self.table.delete(index)

    def _search_item(self):
        if self._check_window(SearchWindow) and self._check_window(AddWindow):
            utility_window = SearchWindow(master=self,
                                          data=self.data)
            self.master.bind('<Button-1>',
                             lambda _e: utility_window.lift())

    def _add_item(self):
        if self._check_window(AddWindow) and self._check_window(SearchWindow):
            add_popup_window = AddWindow(master=self,
                                         data=self.data)
            self.master.bind('<Button-1>',
                             lambda _e: add_popup_window.lift())

    def _check_window(self, obj):
        if obj not in [type(item) for item in self.winfo_children()]:
            return True
        return False

    def fill_table(self):
        for index, data in self.data.data_file.iterrows():
            if pd.isna(data[self.columns[3]]):
                data[self.columns[3]] = None

            self.table.insert(parent='',
                              index='end',
                              iid=index,
                              values=(data[self.columns[0]].capitalize(),
                                      data[self.columns[1]],
                                      data[self.columns[2]],
                                      data[self.columns[3]],
                                      data[self.columns[4]]))

    def erase_binding(self):
        self.master.unbind('<Button-1>')

    def update_table(self):
        self.table.delete(*self.table.get_children())
        self.fill_table()
