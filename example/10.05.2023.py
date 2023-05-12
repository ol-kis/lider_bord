import tkinter as tk

class SubWindow(tk.Frame):
    def __init__(self, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)
        x = tk.Text(self)
        x.pack(expand=1, fill='both')
        

class MainWindow(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self)
        self.win1 = SubWindow(self)
        self.win1.pack(side="left", expand=1, fill=tk.BOTH)
        self.win2 = SubWindow(self)
        self.win2.pack(side="right", expand=1, fill=tk.BOTH)

if __name__ == "__main__":
    main = MainWindow()
    main.mainloop()
