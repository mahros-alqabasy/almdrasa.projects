# Created by Mahros



# Dependencies
import random

# Choice
class Choice:
	def __init__(self, name:str, defeats=""):
		self.name = name
		self.defeats = defeats


	def canDefeat(self, choice):
		return self.defeats == choice


# Player
class Player:
	def __init__(self, name:str, choices:list[Choice]=[], automated=False):
		self.name = name
		self.choices = choices
		self.automated = automated

	def readChoice(self):
		# print("[P]", "Oh! My role!")
		status = False
		userInput = ""

		while not status:
			userInput = input("[?] Rock|Paper|Scissor? ").strip().lower()
			matches = [x for x in self.choices if str(x.name).strip().lower() == userInput]
			if len(matches) == 1:
				return matches[0]
			else:
				print("[!]", "Invalid Choice!, Try Again.")


	def choose(self):
		if not self.automated:
			return self.readChoice()
		else:
			print("[C]", "I will beat you, Human!")
			return random.choice(self.choices)

# Gaeme
class Game:
	def __init__(self, players:list):
		self.players = players
		self.turns = self.selectTurns()
		self.winner = ""

		# history
		"""
			list=[
				(choice, player),
				...
			]
		"""
		self.history:list[tuple] = []


	# Notes
	# The order of players should be random
	# the automated players should be handled by the computer

	# select random turns
	def selectTurns(self):
		# please add a way to randomize this without duplicate
		return self.players

	# banner
	def banner(self):
		print("[*] Starting Game...")
		print("[*] Turns: ", ", ".join([x.name for x in self.turns]))


	def turn(self, name:str):
		print("[*]", name + ",", "Your turn!")

	def displayWinner(self, player:Player):
		print("[*]", player.name.upper(), "is the winner!")

	# start
	def start(self):
		self.banner()
		lastChoice=""
		# logic
		while self.winner.strip() == "":
			for player in self.turns:
				self.turn(player.name)
				lastChoice = player.choose()
				print("[*]", player.name, "choosen", lastChoice.name)
				self.history.append((lastChoice, player))
				self.checker()

		ask = input("[*] Start Game agin? ").strip().lower()
		if ask not in ["no", "n"]:
			self.winner = ""
			self.start()
		else:
			exit()

	# chcker
	def checker(self):
		if len(self.history) < 2:
			return

		c1_choice, c1_player = self.history[0]
		c2_choice, c2_player = self.history[1]
		win = ""

		if c1_choice.name == c2_choice.name:
			print("[@] Very Enthusiastic! Tie.")
			self.history.clear()
			return
		elif c1_choice.canDefeat(c2_choice):
			win = c1_player
		elif c2_choice.canDefeat(c1_choice):
			win = c2_player

		if win:
			self.displayWinner(win)
			self.winner = win.name
			self.history.clear()



# main
def main():
	# define game objects
	choices = {
		"rock":Choice("Rock"),
		"paper":Choice("Paper"),
		"scissor":Choice("Scissor")
	}

	# define defeats
	choices["rock"].defeats = choices["scissor"]
	choices["paper"].defeats = choices["rock"]
	choices["scissor"].defeats = choices["paper"]

	# define players
	user_choices = [choices[choice] for choice in choices]

	players = [
		Player("Mahros", choices=user_choices),
		Player("Computer", choices=user_choices, automated=True)
	]

	# define game
	game = Game(players)


	# run
	game.start()


# run
if __name__ == "__main__":
	try:
		main()
	except Exception as Error:
		print(Error)
