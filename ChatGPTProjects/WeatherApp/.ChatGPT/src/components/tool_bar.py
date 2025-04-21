# Created by Mahros



import tkinter as tk
from src.components.file_path_input import FilePathInput
class ToolBar(tk.Frame):
    def __init__(self, parent, onSave, onOpen):
        super().__init__(parent)

        self.onSaveClicked = onSave
        self.onOpenClicked = onOpen
        self.pack(side="top", fill="x")
        
        self.save_button = tk.Button(self, text="Save", command=self.save_file)
        self.save_button.pack(side="left")
        
        self.open_button = tk.Button(self, text="Open", command=self.open_file)
        self.open_button.pack(side="left")

        self.save_input = FilePathInput(self)
        self.save_input.pack(side="left")

    def save_file(self):
        self.onSaveClicked()
        print("OnSave")

    def open_file(self):
        self.onOpenClicked()
        print("OnOpen")

    def getFilePath(self):
      return self.save_input.getFilePath()
