# Created by Mahros


import tkinter as tk

class EditingArea(tk.Text):
    def __init__(self, parent):
        super().__init__(parent)
        self.config(wrap="word", font=("Arial", 12))
        self.pack(fill="both", expand=True)



    def getValue(self):
      content = self.get("1.0", "end-1c")
      return content

    def setContent(self, content):
      pass

    def clear(self):
      self.delete("1.0", "end-1c")
      
