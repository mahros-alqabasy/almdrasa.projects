import tkinter as tk


class Results(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent, bg='white')
        self.init()

    def init(self):
        self.label_next_player = tk.Label(self, text="Next, Player", bg='white', padx=10, pady=10, font=("Arial", 14))
        self.label_next_player.pack(side="top", expand=True)
        self.label_status = tk.Label(self, text="", bg='white', fg='green', font=("Arial", 14))
        self.label_status.pack(side="top", expand=True)

    def set_next_player(self, player_name, symbol=""):
        self.label_next_player.config(text=f"Next: {player_name}, Symbol: {symbol}")
        self.label_status.config(text="")

    def set_winner(self, winner_name):
        self.label_status.config(text=f"Winner: {winner_name}", fg='green')

    def set_draw(self):
        self.label_status.config(text="Draw!", fg='orange')

    def reset(self):
        self.label_next_player.config(text="Next: Player1, Symbol: X")
        self.label_status.config(text="")