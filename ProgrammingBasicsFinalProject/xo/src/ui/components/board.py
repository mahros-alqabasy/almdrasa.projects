import tkinter as tk

from src.ui.components.cell import Cell

class Board(tk.Frame):
    def __init__(self, parent, on_cell_click=None):
        super().__init__(parent, bd=1, border=2, bg="#ffffff")
        self.on_cell_click = on_cell_click  
        self.cells_items = []
        self.init()
        

    def init(self):
        
        for widget in self.winfo_children():
            widget.destroy()
        self.cells_items = []

        for row in range(3):
            row_cells = []
            for col in range(3):
                cell = Cell(self, row, col, self.on_cell_click)
                cell.grid(row=row, column=col, )
                row_cells.append(cell)
            self.cells_items.append(row_cells)

    def update_cell(self, row, col, value):
        """Update the text/value of a cell (e.g., 'X' or 'O')."""
        cell = self.cells_items[row][col]
        cell.set_value(value)  

    def reset(self):
        for row in self.cells_items:
            for cell in row:
                cell.set_value("")
