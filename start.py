import tkinter as tk
# from PIL import ImageTk, Image
import os
import openpyxl
import datetime
import time

from tkinter import ttk


class Windows(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        # Adding a title to the window
        self.wm_title("Test Application")

        # creating a frame and assigning it to container
        container = tk.Frame(self, height=400, width=600)
        # specifying the region where the frame is packed in root
        container.pack(side="top", fill="both", expand=True)

        # configuring the location of the container using grid
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        # we'll create the frames themselves later but let's add the components to the dictionary.

        frame = Label(container, self, "{i}")
        frame = Label2(container, self, "ljgjeg")
        # lab = Logo(container, self)
        frame.grid(row=0, column=0, sticky="nsew")
        # lab.grid(row=0, column=0, sticky="nsew")


class Label(tk.Frame):
    def __init__(self, parent, controller, text):
        tk.Frame.__init__(self, parent)
        label = tk.Label(
            text=f'{text}',
            fg="black",
            bg="white",
            width=40,
            height=5,
            font=("Times New Roman", 14),
            justify="left",

        )
        label.pack(padx=10, pady=10)


# class Logo(tk.Frame):
#     def __init__(self, parent, controller):
#         tk.Frame.__init__(self, parent)
#         img = Image.open("1-9610-512.gif")
#         img = img.resize((200, 200), Image.ANTIALIAS)
#         my_img = ImageTk.PhotoImage(img)
#         panel = tk.Label(self, image=my_img)


class Label2(tk.Frame):
    def __init__(self, parent, controller, text):
        tk.Frame.__init__(self, parent)
        label2 = tk.Label(
            text=f'{text}',
            fg="black",
            bg="white",
            width=40,
            height=5,
            font=("Times New Roman", 14),
            justify="left",

        )
        label2.pack(padx=10, pady=10)


if __name__ == "__main__":
    testObj = Windows()
    testObj.mainloop()