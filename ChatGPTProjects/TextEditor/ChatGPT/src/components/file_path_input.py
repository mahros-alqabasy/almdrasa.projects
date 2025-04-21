import tkinter as tk
from tkinter import filedialog

class FilePathInput(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.file_path_var = tk.StringVar()
        self.create_widgets()

    def create_widgets(self):
        # Label
        self.label = tk.Label(self, text="Enter or browse for a file:")
        self.label.pack(side="left", padx=5)

        # Entry widget for file path
        self.entry = tk.Entry(self, textvariable=self.file_path_var, width=50)
        self.entry.pack(side="left", padx=5)

        # Browse button
        self.browse_button = tk.Button(self, text="Browse", command=self.browse_file)
        self.browse_button.pack(side="left", padx=5)

    def browse_file(self):
        # Open file dialog and update entry with selected file path
        file_path = filedialog.askopenfilename()
        if file_path:
            self.file_path_var.set(file_path)


    def getFilePath(self):
      return self.file_path_var.get()
