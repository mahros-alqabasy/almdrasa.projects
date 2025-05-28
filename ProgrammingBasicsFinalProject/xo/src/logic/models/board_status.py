from dataclasses import dataclass

from src.logic.player import Player


@dataclass
class BoardStatus:
  winner:Player = None

  def hasWinner(self):
    return self.winner != None

  def __str__(self):
    return f"Status(hasWinner={self.hasWinner()}{f', winner={self._winner.__str__() if self.hasWinner() else ''}'})"
