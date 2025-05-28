# FILE: src/logic/move.py





from src.logic.position import Position
from src.logic.player import Player



  
class Move:
  """doc
    - also for move it's data can't be changed after set.
  """
  _code:str
  _player:Player
  _position:Position
  def __init__(self, position:Position, char:str, player:Player):
    self._code = char
    self._player = player
    self._position = position
    
  def position(self)->Position:
      return self._position if self._position != None else None
    
  def player(self)->Player:
    return self._player
    
  def __str__(self):
    return f"Move({self._code}, player={self._player.__str__()})"