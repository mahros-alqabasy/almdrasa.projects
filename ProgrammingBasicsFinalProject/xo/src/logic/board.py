# FILE:./src/logic/board.py




from src.logic.cell import Cell
from src.logic.move import Move
from src.logic.player import Player
from src.libs.stack.stack import Stack
from src.logic.position import Position
from src.logic.models.board_status import BoardStatus
from src.logic.models.board_config import BoardConfig



"""doc
  - user can change the board size, NxN 
  
  - - - 
  - x -
  - - -
"""
class Board:
  _turnIndex:int
  _config:BoardConfig
  _status:BoardStatus
  _history:Stack[Move]
  _players:list[Player]
  _cells:list[list[Cell]]

  def __init__(self, size:int = 3, players:list[Player] = []):
    self._size = size
    self._players = players
    
    # init board cells
    self.init()
  
  def checkWinner(self)->BoardStatus:
    """doc
    
      [x] winner rules: # not effecient
        - any row has the same player
        - any column has the same player
        - any of x or -x has the same player
        
      [*] approach:
        - instead of checking for all board, just check the winner BEFORE every move,
          you may ask me "why not AFTER?", because before any move there may be a winner, 
          so that we should't able the player to apply any move.
    """
    
    lastPlayer = self.lastMove()
    
    if lastPlayer == None:
      self._status = BoardStatus(None)
      return self._status
    
    lastPlayer = lastPlayer.player()

    # checkrows
    for row in self._cells:
      if all(x.move() != None and x.move().player() == lastPlayer for x in row):
        print('Winner, in rows')
        self._status = BoardStatus(lastPlayer)
        return self._status
    
    
    # check cols
    for col in range(self._size):
      col_data = [self._cells[row][col] for row in range(self._size)]
      if all(x.move() != None and x.move().player() == lastPlayer for x in col_data):
        print('Winner, in cols')
        self._status = BoardStatus(lastPlayer)
        return self._status
      
    # check cross
    cross1 = [self._cells[i][i] for i in range(self._size)]
    cross2 = [self._cells[i][self._size - 1 - i] for i in range(self._size)]
    
    if all(x.move() != None and x.move().player() == lastPlayer for x in cross1):
      print('Winner, in cross1')
      self._status = BoardStatus(lastPlayer)
      return self._status
    
    if all(x.move() != None and x.move().player() == lastPlayer for x in cross2):
      print('Winner, in cross2')
      self._status = BoardStatus(lastPlayer)
      return self._status
    
    
    self._status = BoardStatus(None)
    return self._status
  
  def lastMove(self)->Move:
    "we will return cell instead of move, because we need the Move position"
    return self._history.top() if self._history.isNotEmpty() else None
    
  
  def redo(self):
    move = self._history.pop()
    self._cells[move.position().row()].pop(move.position().col())
    
  def nextTurnIndex(self) -> int:
    return (self._turnIndex + 1) % len(self._players)
       
  def nextTurnPlayer(self)->Player:
    return self._players[self.nextTurnIndex()]
  
  def applyMove(self, position:Position):    
      player:Player = self.nextTurnPlayer()
      move:Move = Move(position, '', player)
      if self.isValidMove(move):
        self._cells[position.row()][position.col()].fill(move)
      else:
        return False

      self._history.push(move)
      self._status = self.checkWinner()
      if self._status.hasWinner() and self._status.winner != self._history.top().player() :
          print("Can't apply move")
          self.redo()
          return False

      self._turnIndex = self.nextTurnIndex()
      return True
    
  def isValidMove(self, move:Move):
    target:Cell = self._cells[move.position().row()][move.position().col()]
    checks:list[bool] = [
      self.isValidPosition(move.position()),   
      not target.filled(),
      self.isCorrectTurn(move.player())
    ]

    # all checks must be true
    return all(checks)

  def isCorrectTurn(self, player:Player):
    return player != self._players[self._turnIndex]
  
  def isValidPosition(self, position:Position):
    if position.row() in range(self._size) and position.col() in range(self._size):
      return True
    
    return False
  
  
  # end
  def reset(self):
    for row in range(self._size):
      cols = [Cell(Position(row=row, col=col)) for col in range(self._size)]
      self._cells.append(cols)
  
  def init(self):
    self._cells = []
    self._turnIndex = 0 
    self._history = Stack()
    self._status = BoardStatus(None)
    self.reset()
    
  def __str__(self):
    return f"Board(size={self._size}, cells={self._cells})"
  
  def display(self):
    for row in self._cells:
      for cell in row:
        print(f'{f'{cell.position().row()},{cell.position().col()}' if not cell.filled() else f' {cell.move().player().name[0]} '}   ', end='')
        
      print()
      print()
