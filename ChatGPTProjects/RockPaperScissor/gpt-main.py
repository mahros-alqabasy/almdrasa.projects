# Created by Mahros


"""
Rock-Paper-Scissors Game
Author: Mahros
Description: A command-line Rock-Paper-Scissors game featuring human and computer players.
"""

import random
from typing import List, Tuple

class Choice:
    """
    Represents a game choice (Rock, Paper, or Scissors).
    """

    def __init__(self, name: str):
        """
        Initializes a Choice instance.

        :param name: The name of the choice.
        """
        self.name = name
        self.defeats = None  # Will be set after all choices are created

    def can_defeat(self, other_choice: 'Choice') -> bool:
        """
        Determines if this choice defeats another choice.

        :param other_choice: The choice to compare against.
        :return: True if this choice defeats the other, False otherwise.
        """
        return self.defeats == other_choice

class Player:
    """
    Represents a player in the game.
    """

    def __init__(self, name: str, choices: List[Choice], automated: bool = False):
        """
        Initializes a Player instance.

        :param name: The name of the player.
        :param choices: A list of possible choices.
        :param automated: Indicates if the player is controlled by the computer.
        """
        self.name = name
        self.choices = choices
        self.automated = automated

    def read_choice(self) -> Choice:
        """
        Prompts the user to select a choice.

        :return: The selected Choice object.
        """
        while True:
            user_input = input("[?] Rock | Paper | Scissors? ").strip().lower()
            for choice in self.choices:
                if choice.name.lower() == user_input:
                    return choice
            print("[!] Invalid choice. Please try again.")

    def choose(self) -> Choice:
        """
        Determines the player's choice.

        :return: The selected Choice object.
        """
        if self.automated:
            print(f"[C] {self.name} is making a choice...")
            return random.choice(self.choices)
        else:
            return self.read_choice()

class Game:
    """
    Manages the Rock-Paper-Scissors game.
    """

    def __init__(self, players: List[Player]):
        """
        Initializes a Game instance.

        :param players: A list of Player objects.
        """
        self.players = players
        self.history: List[Tuple[Choice, Player]] = []
        self.winner: str = ""

    def select_turns(self) -> List[Player]:
        """
        Randomizes the order of player turns.

        :return: A list of Player objects in randomized order.
        """
        turns = self.players[:]
        random.shuffle(turns)
        return turns

    def banner(self, turns: List[Player]):
        """
        Displays the game banner and turn order.

        :param turns: The list of Player objects in turn order.
        """
        print("[*] Starting Game...")
        print("[*] Turn order: " + ", ".join(player.name for player in turns))

    def display_winner(self, player: Player):
        """
        Announces the winner of the game.

        :param player: The winning Player object.
        """
        print(f"[*] {player.name.upper()} is the winner!")

    def checker(self):
        """
        Checks the game history to determine if there's a winner.
        """
        if len(self.history) < 2:
            return

        c1_choice, c1_player = self.history[0]
        c2_choice, c2_player = self.history[1]

        if c1_choice.name == c2_choice.name:
            print("[@] It's a tie!")
            self.history.clear()
            return

        if c1_choice.can_defeat(c2_choice):
            winner = c1_player
        else:
            winner = c2_player

        self.display_winner(winner)
        self.winner = winner.name
        self.history.clear()

    def start(self):
        """
        Starts the game loop.
        """
        while True:
            turns = self.select_turns()
            self.banner(turns)
            self.winner = ""

            while not self.winner:
                for player in turns:
                    print(f"[*] {player.name}, it's your turn!")
                    choice = player.choose()
                    print(f"[*] {player.name} chose {choice.name}")
                    self.history.append((choice, player))
                    if len(self.history) == 2:
                        self.checker()
                        if self.winner:
                            break

            play_again = input("[*] Play again? (yes/no): ").strip().lower()
            if play_again not in ("yes", "y"):
                print("[*] Thanks for playing!")
                break

def main():
    """
    Main function to set up and start the game.
    """
    # Define choices
    rock = Choice("Rock")
    paper = Choice("Paper")
    scissors = Choice("Scissors")

    # Set defeating relationships
    rock.defeats = scissors
    paper.defeats = rock
    scissors.defeats = paper

    choices = [rock, paper, scissors]

    # Define players
    players = [
        Player("Mahros", choices=choices),
        Player("Computer", choices=choices, automated=True)
    ]

    # Start the game
    game = Game(players)
    game.start()

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"[!] An error occurred: {e}")


