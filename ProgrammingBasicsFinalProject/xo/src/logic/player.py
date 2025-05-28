# FILE: src/logic/player.py


class Player:
  def __init__(self, name:str = 'Mahros'):
    self.name = name
    
  def __str__(self):
    return f"Player(name={self.name})"
  