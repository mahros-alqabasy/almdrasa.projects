# FILE: src/logic/game.py

# imports
from logic.board import Board
from logic.player import Player



class Game:
  """doc
    - I will represent the game logic and state.
    - It will handle the game rules, player turns, and game state.
    - It will manage the game flow and interactions between players.
  """  
  
  players:list[Player] = [
    Player("Mahros", 'X'),
    Player("Computer", 'O')
  ]
  board:Board = Board(players=players)
  
  
    