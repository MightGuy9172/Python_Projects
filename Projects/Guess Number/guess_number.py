#Guess the number

import random 

EASY=10
HARD=5

def guesser(guess,choosen,lives):
  if(guess==choosen):
    print(f"You Guessed right number {choosen}")
  elif guess > choosen:
    print("Lower the Guess")
    return lives-1
  else:
    print("Higher the Guess")
    return lives-1


def level():
  difficulty=input("Choose a difficulty. Type 'easy' or 'hard' : ").lower()
  if difficulty=='easy':
    return EASY
  else:
    return HARD


def game():
  art= r""" 
                                                     _                
                                                    | |               
   __ _ _   _  ___  ___ ___    _ __  _   _ _ __ ___ | |__   ___ _ __  
  / _` | | | |/ _ \/ __/ __|  | '_ \| | | | '_ ` _ \| '_ \ / _ \ '__| 
 | (_| | |_| |  __/\__ \__ \  | | | | |_| | | | | | | |_) |  __/ |    
  \__, |\__,_|\___||___/___/  |_| |_|\__,_|_| |_| |_|_.__/ \___|_|    
  __/ |                                                              
  |___/  
  """

  print(art)
  print("Welcome to number Guessing Game")
  print("I am thinking of number between 1 and 100")
  choosen=random.randint(1,100)
  
  
  lives=level()
  
  guess=0
  while guess!=choosen:
    print(f"You have {lives} turns remaining.")
    guess=int(input("Guess the number: "))
    lives=guesser(guess,choosen,lives)
    if lives==0:
      print("You run out of Guess. You lose")
      return

game()