# FILE: ./app.py
from src.logic.board import Board
from src.logic.player import Player
from src.logic.position import Position


if __name__ == "__main__":
  players:list[Player] = [
    Player('Mahros'), Player('Ahmed')
  ]
  
  board:Board = Board(players=players)
  
  # for row in range(3):
  #   for col in range(3):
  #     board.applyMove(position=Position(row,col))
  
  board.applyMove(position=Position(0,0))
  board.applyMove(position=Position(1,0))
  board.applyMove(position=Position(0,1))
  board.applyMove(position=Position(1,1))
  board.applyMove(position=Position(0,2)) 
  


  board.display()