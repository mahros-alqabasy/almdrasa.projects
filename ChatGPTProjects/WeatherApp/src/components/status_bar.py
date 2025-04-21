# Created by Mahros



import tkinter as tk

class StatusBar(tk.Label):
    def __init__(self, parent):
        super().__init__(parent, text="Ready", bd=1, relief="sunken", anchor="w")
        self.pack(side="bottom", fill="x")

    def update_status(self, text):
        self.config(text=text)

    def showMessage(self, msg):
      self.config(text=msg)


