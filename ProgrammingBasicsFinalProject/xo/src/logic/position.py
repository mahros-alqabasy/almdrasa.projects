# FILE: src/logic/position.py



class Position:
  """doc
    - this position has:
      row, col they can't not be changed after they set.
  """
  _row:int
  _col:int
  def __init__(self, row:int, col:int):
    self._row = row if row >= 0 else None 
    self._col = col if col >= 0 else None
  
  def row(self) -> int:
    return self._row

  def col(self) -> int:
    return self._col
  
  def pos(self) -> tuple:
    return (self._row, self._col)

  
  def __str__(self):
    return f"Position(row={self._row}, col={self._col})"