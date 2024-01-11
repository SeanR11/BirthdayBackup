from birthday_planner import BirthdayPlanner
from tkinter import Tk, Canvas, Frame
from buttons import TextButton
from settings import Settings
from data import Data


def Main():
    main_window = Tk()
    main_window.title("Birthday Backup")
    width = 800
    height = 600
    main_window.geometry(f'{width}'
                         f'x{height}'
                         f'+{int((main_window.winfo_screenwidth() / 2) - width / 2)}'
                         f'+{int((main_window.winfo_screenheight() / 2) - height / 2)}')

    data = Data()

    main_window.config(bg='#45FFCA')

    logo = Canvas(master=main_window, width=300, height=150, highlightthickness=0, bg=main_window['bg'])
    logo.create_image(150, 75, image=data.logo)
    logo.place(x=(width * 0.5) - 150, y=height * 0.08)

    menu_frame = Frame(master=main_window,
                       bg=main_window['bg'],
                       width=300,
                       height=300)
    menu_frame.place(x=(width * 0.5) - 150,
                     y=height * 0.35)
    menu_padding = {'x': 0,
                    'y': 30
                    }

    birthday_list_btn = TextButton(master=menu_frame,
                                   text='Birthday Planner',
                                   command=lambda: BirthdayPlanner(master=main_window,
                                                                   data=data))
    birthday_list_btn.pack(padx=menu_padding['x'],
                           pady=menu_padding['y'])

    settings_btn = TextButton(master=menu_frame,
                              text='Settings',
                              command=lambda: Settings(master=main_window,
                                                       data=data))
    settings_btn.pack(padx=menu_padding['x'],
                      pady=menu_padding['y'])

    exit_btn = TextButton(master=menu_frame,
                          text='Exit',
                          command=main_window.destroy)
    exit_btn.pack(padx=menu_padding['x'],
                  pady=menu_padding['y'])

    main_window.resizable(width=False,
                          height=False)
    main_window.mainloop()


if __name__ == '__main__':
    Main()
