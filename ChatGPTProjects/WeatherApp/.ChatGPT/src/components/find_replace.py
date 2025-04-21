import tkinter as tk
from tkinter import simpledialog

class FindReplace:
    def __init__(self, text_widget):
        self.text_widget = text_widget

    def find(self):
        search_term = simpledialog.askstring('Find', 'Enter text to find:')
        if search_term:
            start_idx = '1.0'
            while True:
                start_idx = self.text_widget.search(search_term, start_idx, stopindex='end')
                if not start_idx:
                    break
                end_idx = f'{start_idx}+{len(search_term)}c'
                self.text_widget.tag_add('highlight', start_idx, end_idx)
                start_idx = end_idx
            self.text_widget.tag_configure('highlight', background='yellow')

    def replace(self):
        search_term = simpledialog.askstring('Find', 'Enter text to find:')
        replace_term = simpledialog.askstring('Replace', 'Enter replacement text:')
        if search_term and replace_term:
            content = self.text_widget.get('1.0', 'end-1c')
            updated_content = content.replace(search_term, replace_term)
            self.text_widget.delete('1.0', 'end-1c')
            self.text_widget.insert('1.0', updated_content)
