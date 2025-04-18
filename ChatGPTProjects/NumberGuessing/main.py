# Created by Mahros


# packages
import random


# procedures
# ask user to choose range
# then make a random runber form this range
# user enter his number 
# then checker function should run to estimate how near the guess and random
# then if he guess correct run won function


class Game:
  _range = ()
  def __init__(self):
    pass

  def won(self):
    print("Congrats! You WON.")
    exit(0)

    
  def get_range(self):
    numbers_range = input("What is range (ex. 1, 5)? ")
    left, right = numbers_range.split(",")
    
    self._range = (int(left), int(right))
    return self._range

  def select_random(self):
    value = random.randint(self._range[0], self._range[1]) 
    return value


  def checker(self, guessed, random):
    if guessed == random:
      self.won()
    elif guessed > random:
      print(f"Less than {guessed}")
    elif guessed < random:
      print(f"Greater than {guessed}")
    

  def get_guessed(self):
    number = int(input(f"Now! Guess between {self._range[0]}, {self._range[1]}? "))

    if number >= self._range[0] and number <= self._range[1]:
      return number

    print("Number must be in range!")
    
    
  def run(self):
    self.get_range()
    random_int = self.select_random()
    while True:
      guessed_int = self.get_guessed()
      self.checker(guessed_int, random_int)

      
      
      



def main():
  print("Main")
  game = Game()
  game.run()

# run
if __name__ == "__main__":
  main()
