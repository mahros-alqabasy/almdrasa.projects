import tkinter as tk
import src.logic.move as logic_move


class Cell(tk.Frame):
  _value:logic_move.Move
  def __init__(self, parent, row, col, on_cell_click=None):
    super().__init__(parent, bd=1, bg="white", width=50, height=50)
    self.row = row
    self.col = col
    self.on_cell_click = on_cell_click

    self.init()


  def set_value(self, value):
    self.cell_container.config(text=value if value else " ")


  def updateValue(self, vlaue:logic_move.Move):
    self._value = vlaue
    
    # update the values
    self.refresh()
    
    
  def refresh(self):
    pass
  
  def handle_click(self):
    if self.on_cell_click:
      self.on_cell_click(self.row, self.col)
  
  def init(self):
    self.cell_container = tk.Button(
      self, text="", 
      background="#ffebee", foreground="black", font="cairo", width=8, height=2,
      relief=tk.RIDGE,
      border=1,
      borderwidth=5,
      bd=2,
      highlightbackground="blue", highlightthickness=1,
      command=self.handle_click,
      highlightcolor="red",
      
    )
    
    self.cell_container.pack( anchor='center')