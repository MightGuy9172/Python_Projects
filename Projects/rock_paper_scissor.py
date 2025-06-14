#Rock paper Scissors
import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

action=[rock,paper,scissors]

print("What do you choose? Type 0 for Rock, 1 for Paper and 2 for Scissors.")
user=int(input())
if user >= 3 or user < 0: 
  print("You typed an invalid number, you lose!") 
else:
  print(action[user])


print("Computer choose:")
computer=random.randint(0,len(action)-1)
print(action[computer])

if user==0 and computer==2:
  print("You Win")
elif user==0 and computer==1:
  print("You Lose")
elif user==1 and computer==2:
  print("You Lose")
elif user==1 and computer==0:
  print("You Win")
elif user==2 and computer==0:
  print("You Lose")
elif user==2 and computer==1:
  print("You Win")
else:
  print("Draw")