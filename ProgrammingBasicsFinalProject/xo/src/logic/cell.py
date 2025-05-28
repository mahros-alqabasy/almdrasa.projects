# FILE:./src/logic/cell.py

from src.logic.position import Position
from src.logic.move import Move


"""doc.logic.cell
  - i will write the cell doc here
"""
class Cell:
  _move:Move = None
  _position:Position = None
  
  
  def __init__(self, position:Position):
    self._position = position
    
  def fill(self, move:Move)->None:
    self._move = move
  
  def filled(self)->bool:
    return self.move() != None
  
  def position(self)->Position:
    return self._position
  
  def move(self)->Move:
    return self._move
  
  def __str__(self):
    return f"Cell(pos={self._position.__str__()}{f', move={self._move.__str__()}' if self._move != None else ''})"
  
