import tkinter as tk
import os
# import openpyxl
import datetime
import time
from itertools import cycle
from tkinter import *
from multiprocessing import Process


# from tkinter import ttk


class windows(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.wm_title("Федерация функционального многоборья")
        # self.configure(background='yellow')


class Atlets(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.atlets_now = tk.Label(text=f'Hello', fg="black", bg="pink", width=50, height=10,
                                   font=("Times New Roman", 14), justify="left", )
        self.atlets_next = tk.Label(text=f'Hello', fg="black", bg="red", width=50, height=10,
                                    font=("Times New Roman", 14), justify="left", )
        self.atlets_now.pack(side=RIGHT, padx=5, pady=5, anchor="n")
        self.atlets_next.pack(side=RIGHT, padx=5, expand=True, anchor="s")

    def update_atlets(self, window):
        for i in range(12, 50, 5):
            # self.atlets_now["text"] = f'\nЗаход:{sheet.cell(row=i, column=2).value} \
            #     \nСейчас на поле следующие атлеты: \n\t{str(sheet.cell(row=i + 1, column=3).value)}\
            #                                         \n\t{str(sheet.cell(row=i + 2, column=3).value)}\
            #                                         \n\t{str(sheet.cell(row=i + 3, column=3).value)}\
            #                                         \n\t{str(sheet.cell(row=i + 4, column=3).value)}'
            self.atlets_now["text"] = f'New {i}'
            self.atlets_next["text"] = f'Old {i}'
            time.sleep(2)
            window.update()
        window.mainloop()

    # def get_list_of_athletes(self):
    #     wb = openpyxl.load_workbook(filename='Тайминг 23 апреля.xlsx', data_only=True)
    #     sheet = wb["Лист1"]
    #     return sheet


class App(tk.Frame):
    def __init__(self, parent, controller, image_files, delay):
        tk.Frame.__init__(self, parent)
        self.delay = delay
        self.pictures = cycle((tk.PhotoImage(file=image), image)
                              for image in image_files)
        self.picture_display = tk.Label(controller)
        self.picture_display.pack()

    def show_slides(self):
        img_object, img_name = next(self.pictures)
        self.picture_display.config(image=img_object)
        self.after(self.delay, self.show_slides)

    def run(self):
        self.mainloop()


if __name__ == "__main__":
    testObj = windows()
    container = tk.Frame(testObj, height=600, width=600)
    container.pack()
    array = Atlets(container, testObj)
    frame = array

    image_files = [
        'sticker_vk_bestsummerever_020.gif',
        'sticker_vk_bestsummerever_021.gif',
        'sticker_vk_bestsummerever_022.gif',
        'sticker_vk_bestsummerever_023.gif',
        'sticker_vk_bestsummerever_024.gif'
    ]
    delay = 3500
    app = App(container, testObj, image_files, delay)
    frame = app
    frame.pack()

    p1 = Process(target=app.show_slides())
    p1.start()
    p2 = Process(target=array.update_atlets(testObj))
    p2.start()
    p1.join()
    p2.join()

