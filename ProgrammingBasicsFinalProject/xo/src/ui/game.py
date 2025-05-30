# src/weather_app.py

import tkinter as tk
import src.ui.gui as gui
import src.logic.board as logic_board
from src.ui.components.board import Board
from src.ui.components.results import Results
import src.logic.player as logic_player
import src.logic.position as logic_position

import src.libs.sound_unit.sound_unit as sound_unit

class Game(gui.Gui):
	board_model:logic_board.Board
	
	def __init__(self, su:sound_unit.SoundUnit):
		self.su = su
		conf = gui.AppConf(window=gui.WindowConf(title="XO Game", size=(450, 500)))
		super().__init__(conf)
		self.players = [logic_player.Player("Mahros", "X"), logic_player.Player("Ahmed", "O")]

		self.init_game()
		self.init_widgets()

	def init_game(self):
		self.board_model = logic_board.Board(size=3, players=self.players)
		self.current_player_index = 0

	def init_widgets(self):
		# widgets    
		self.results = Results(self.root)
		self.results.pack(side="top", fill="x", anchor="n", expand=True)

		# reset button
		self.reset_button = tk.Button(self.root, text="Reset", command=lambda : self.reset_game())
		self.reset_button.pack(side="top")
  
  
		self.board = Board(self.root, on_cell_click=self.handle_cell_click)
		self.board.pack(side="top", fill="y",  expand=True)
		self.results.set_next_player(self.players[self.current_player_index].name)

  
  
	def handle_cell_click(self, row, col):
		print("clicked")
		self.su.play_move()
		# Prevent move if game is over
		if self.board_model._status.hasWinner():
			self.su.play_win()
			return
    
		if self.is_draw():
			self.su.play_draw()
			return
 
		position = logic_position.Position(row=row, col=col)
		

		move_result = self.board_model.applyMove(position)
		if not move_result:
				return
  
		# Update UI
		player = self.players[self.current_player_index]
		self.board.update_cell(row, col, player.symbol)
  
		# Check for winner
		if self.board_model._status.hasWinner():
			winner = self.board_model._status.winner
			self.results.set_winner(winner.name)
			self.su.play_win()
			return
 
		# Check for draw
		if self.is_draw():
			self.results.set_draw()
			return
 
 
		# Next turn
		self.current_player_index = self.board_model._turnIndex
		self.results.set_next_player(self.players[self.current_player_index].name, self.players[self.current_player_index].symbol)
  
  
		# run sound for move


		

	def is_draw(self):
		
		for row in self.board_model._cells:
			for cell in row:
				if not cell.filled():
					return False
		return not self.board_model._status.hasWinner()

	def reset_game(self):
		self.init_game()
		self.board.reset()
		self.results.reset()


