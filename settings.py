from email_birthday_script import email_birthday_script
from buttons import ImageButton, TextButton
from tkinter import Frame, Label, Canvas
from plyer import notification
import tkinter as tk
import os


class Settings(tk.Frame):
    def __init__(self, master, data):
        super().__init__(master=master)

        self['bg'] = self.master['bg']
        self['width'] = self.master.winfo_width()
        self['height'] = self.master.winfo_height()
        self.pack_propagate(False)
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
                              text='Settings',
                              borderwidth=0,
                              bg=self.header_frame['bg'],
                              font=('david', 30))
        self.headline.place(x=self['width'] * 0.42,
                            y=10)

        self.main_frame = Frame(master=self,
                                bg=master['bg'],
                                width=self['width'],
                                height=self['height'] * 0.9)
        self.main_frame.pack()

        if os.path.exists(f'{os.getenv("APPDATA")}\\Microsoft\\Windows\\Start Menu\\Programs\\Startup\\BirthdayPlanner.bat'):
            checkbox_state = 'checked_box'
            _command = self._cancel_run_on_startup
        else:
            checkbox_state = 'unchecked_box'
            _command = self._run_on_startup

        self.add_checkbox = Canvas(master=self.main_frame,
                                   width=80, height=80,
                                   highlightthickness=0,
                                   bg=self['bg'])
        self.add_checkbox.create_image(40, 40,
                                       image=self.data.images[checkbox_state],
                                       tags='image')
        self.add_checkbox.place(x=self['width'] * 0.3,
                                y=self['height'] * 0.17)

        self.auto_startup_btn = TextButton(master=self.main_frame,
                                           text='Run on startup',
                                           size=25,
                                           command=_command)
        self.auto_startup_btn.place(x=self['width'] * 0.39,
                                    y=self['height'] * 0.20)

        self.manual_email_btn = TextButton(master=self.main_frame,
                                           text='Send emails manual',
                                           size=25,
                                           command=email_birthday_script)
        self.manual_email_btn.place(x=self['width'] * 0.33,
                                    y=self['height'] * 0.40)


        self.pack()

    def _run_on_startup(self):
        startup_path = f'{os.getenv("APPDATA")}\\Microsoft\\Windows\\Start Menu\\Programs\\Startup\\BirthdayPlanner.bat'
        if not os.path.exists(startup_path):
            with open(startup_path, 'w+') as batFile:
                batFile.write(f'{os.getcwd()[:2]}\n'
                              f'cd {os.getcwd()[3:]}\n'
                              f'python email_birthday_script.py\n'
                              f'exit')
                notification.notify(title='BirthdayPlanner',
                                    message='Run on startup activated',
                                    app_icon=None,
                                    timeout=10)
                self.auto_startup_btn.config(command=self._cancel_run_on_startup)
                self.add_checkbox.itemconfigure(tagOrId='image',
                                                image=self.data.images['checked_box'])

    def _cancel_run_on_startup(self):
        path = f'{os.getenv("APPDATA")}\\Microsoft\\Windows\\Start Menu\\Programs\\Startup\\BirthdayPlanner.bat'
        if os.path.exists(path):
            os.remove(path)
            notification.notify(title='BirthdayPlanner',
                                message='Run on startup cancaled',
                                app_icon=None,
                                timeout=10)
        self.auto_startup_btn.config(command=self._run_on_startup)
        self.add_checkbox.itemconfigure(tagOrId='image',
                                        image=self.data.images['unchecked_box'])
