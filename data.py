from tkinter import PhotoImage
import pandas as pd


class Data:
    def __init__(self):
        self.font = 'David'
        self.logo = PhotoImage(file='resources/Logo.png')
        self.buttons = {'return': PhotoImage(file='resources/return.png'),
                        'trash': PhotoImage(file='resources/trash.png'),
                        'search': PhotoImage(file='resources/search.png'),
                        'add': PhotoImage(file='resources/add.png')
                        }
        self.images = {'checked_box': PhotoImage(file='resources/checked.png'),
                       'unchecked_box': PhotoImage(file='resources/unchecked.png')
                       }
        self.data_file = pd.read_csv(filepath_or_buffer=f'resources/birthdays.csv',
                                     index_col=False).copy()

    def update_file(self):
        self.data_file.to_csv(path_or_buf=f'resources/birthdays.csv',
                              index=False)
