# Number Guessing Game
# Created by Mahros, improved for awesomeness

import random


class Game:
    def __init__(self):
        self._range = (0, 0)
        self.target_number = None

    def won(self, attempts):
        print(f"\n🎉 Congrats! You guessed it right in {attempts} attempt(s)!")
    
    def get_range(self):
        while True:
            try:
                numbers_range = input("Enter a range (e.g., 1, 10): ")
                left, right = map(int, numbers_range.strip().split(","))
                if left >= right:
                    print("Left number must be less than right number.")
                    continue
                self._range = (left, right)
                return
            except ValueError:
                print("Invalid format. Please enter two numbers separated by a comma.")

    def select_random(self):
        self.target_number = random.randint(self._range[0], self._range[1])

    def get_guessed(self):
        while True:
            try:
                guess = int(input(f"Guess a number between {self._range[0]} and {self._range[1]}: "))
                if self._range[0] <= guess <= self._range[1]:
                    return guess
                else:
                    print("Number is out of range.")
            except ValueError:
                print("Please enter a valid integer.")

    def checker(self, guessed):
        if guessed > self.target_number:
            print("Too high! Try something lower.")
        elif guessed < self.target_number:
            print("Too low! Try something higher.")

    def run(self):
        self.get_range()
        self.select_random()
        attempts = 0

        while True:
            guess = self.get_guessed()
            attempts += 1
            if guess == self.target_number:
                self.won(attempts)
                break
            self.checker(guess)


def main():
    print("🎮 Welcome to the Number Guessing Game!")
    while True:
        game = Game()
        game.run()
        play_again = input("Do you want to play again? (yes/no): ").strip().lower()
        if play_again not in ("yes", "y"):
            print("Thanks for playing! Goodbye 👋")
            break


# Run the game
if __name__ == "__main__":
    main()
