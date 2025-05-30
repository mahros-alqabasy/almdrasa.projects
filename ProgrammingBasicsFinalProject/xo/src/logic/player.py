# FILE: src/logic/player.py


class Player:
    def __init__(self, name: str = "Mahros", symbol='x or o'):
        self.name = name

        self.symbol = symbol
    def __str__(self):
        return f"Player(name={self.name})"
