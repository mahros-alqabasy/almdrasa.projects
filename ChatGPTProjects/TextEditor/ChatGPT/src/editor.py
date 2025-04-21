import tkinter as tk
from src.components.tool_bar import ToolBar
from src.components.status_bar import StatusBar
from src.components.line_numbers import LineNumbers
from src.components.syntax_highlighter import SyntaxHighlighter
from src.components.find_replace import FindReplace

class Editor:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title('Enhanced Text Editor')
        self.root.geometry('800x600')

        # text widget
        self.text_widget = tk.Text(self.root, wrap='word', undo=True)

        self.find_replace = FindReplace(self.text_widget)
        self.tool_bar = ToolBar(self.root, self.find_replace.find, self.find_replace.replace)
        self.tool_bar.pack(side='top', fill='x')


        self.text_widget.pack(side='right', fill='both', expand=True)

        self.line_numbers = LineNumbers(self.root, self.text_widget)
        self.syntax_highlighter = SyntaxHighlighter(self.text_widget)


        # file


        self.status_bar = StatusBar(self.root)
        self.status_bar.pack(side='bottom', fill='x')

        self.root.mainloop()
