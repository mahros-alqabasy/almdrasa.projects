import os
import pygame

class SoundUnit:
    def __init__(self, sounds_directory=None):
        self.SOUNDS_DIR = sounds_directory
        pygame.mixer.init()

    def _sound_path(self, filename: str):
        if self.SOUNDS_DIR:
            return os.path.join(self.SOUNDS_DIR, filename)
        return filename

    def play_move(self):
        self._play("move.wav")

    def play_win(self):
        self._play("win.wav")

    def play_draw(self):
        self._play("draw.wav")

    def _play(self, filename: str):
        path = self._sound_path(filename)
        try:
            sound = pygame.mixer.Sound(path)
            sound.play()
        except Exception as e:
            print(f"Error playing sound '{filename}': {e}")
