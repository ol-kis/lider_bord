from tkinter import *
import random
from PIL import ImageTk, Image

win = Tk()
win.attributes('-fullscreen', True)
# Define Frame Class

class MyFrame:
    def __init__(self, master, **kwargs):
        frame = Frame(master, **kwargs)
        frame.pack()

def FrameOne():
    frameone = MyFrame(win, width = win.winfo_screenwidth(),
                       height = win.winfo_screenheight()//3,
                       bg='black')
def FrameTwo():
    frametwo = MyFrame(win, width=win.winfo_screenwidth(),
                       height = win.winfo_screenheight()//3,
                       bg='blue')
def FrameThree():
    framethree = MyFrame(win, width=win.winfo_screenwidth(),
                       height = win.winfo_screenheight()//3,
                       bg='red')

#Call Frame (This is where I want the following frames to have different unique attributes)

FrameOne()
FrameTwo()
FrameThree()

win.mainloop()