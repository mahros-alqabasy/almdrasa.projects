import os
import sys





from src.ui.game import Game
import src.libs.sound_unit.sound_unit as soud_unit


if __name__ == "__main__":
    # try:
    # su = soud_unit.SoundUnit(os.path.abspath(".").join('src/assets/sounds/'))
    su = soud_unit.SoundUnit('src/assets/sounds/')
    game = Game(su)
    game.run()
    # except Exception as Error:
    #     print(f"I am so sorry, i forgot to handle this error: {Error}")
    #     print("Please, just restart the game.")