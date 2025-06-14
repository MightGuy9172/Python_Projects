#Hangman game

import random
import art
import words

stages = art.stages

end_of_game = False
word_list = words.word_list
chosen_word = random.choice(word_list)
word_length = len(chosen_word)


print(art.logo)

display = []
for _ in range(word_length):
    display += "_"

lives=6

while not end_of_game:
    guess = input("Guess a letter: ").lower()
    if guess in display:
      print(f"You already guessed the letter: {guess}")
    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter
        
          
    print(f"{' '.join(display)}")
    
    if guess not in chosen_word:
      print(f"You guessed wrong letter {guess}.You Lose a life.")
      lives-=1
      if lives==0:
        end_of_game=True
        print("\nYou Lose")
 
    if "_" not in display:
        end_of_game = True
        print("\nYou win.")
      
    print(stages[lives])