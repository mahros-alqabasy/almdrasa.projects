# Created by Mahros


# Hi!
# This project hasn't completed yet.
# But! It is still good for me
# I will work on it in the future 
# It Information from ALMDRASA.COM site
# Then convert it to MODELS using OOP
# This project is SCALABLE as any one can update on it.



# Dependencies
from src import almdrasa as almdrasa
from src.utils import logger as log

# main
def main():
  # Set Scrapper for the hacker news
  sc = almdrasa.Almdrasa(verbose=True)
  for person in sc.about_us_persons():
    person.display()
  

# run
if __name__ == "__main__":
  try:
    main()
  except Exception as Error:
    print(Error)

