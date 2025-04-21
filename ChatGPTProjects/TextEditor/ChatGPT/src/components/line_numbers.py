import tkinter as tk

class LineNumbers(tk.Canvas):
    def __init__(self, parent, text_widget):
        super().__init__(parent, width=40, bg='lightgray', bd=0, highlightthickness=0)
        self.text_widget = text_widget
        self.text_widget.bind('<KeyRelease>', self.update_line_numbers)
        self.text_widget.bind('<Configure>', self.update_line_numbers)
        self.update_line_numbers()
        self.pack(side='left', fill='y')

    def update_line_numbers(self, event=None):
        self.delete('all')
        line_count = int(self.text_widget.index('end-1c').split('.')[0])
        for i in range(1, line_count + 1):
            self.create_text(2, i * 20, anchor='nw', text=str(i), font=('Courier', 10))
