import tkinter as tk

class Gui:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title('Enhanced Text Editor')
        self.root.geometry('800x600')

    def run(self):
        self.root.mainloop()
