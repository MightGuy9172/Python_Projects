#Treasure Game

print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')


print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

print('You are at cross road. Where  do you want to go? "left" or "right"')
dir=input()

if dir=="left":
  print('You came to a lake. There is an island in the middle of the lake. Type "wait" for wait for boat. Type "swim" to swim across.')
  action=input()

  if action=="wait":
    print('You arrived at an island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which colour do you choose?')
    color=input()

    if color=="yellow":
      print("You found the Treasure. You Win.")
    elif color=="red":
      print("You entered a room of Fire. Game Over.")
    elif color=="blue":
      print("You entered a room of Beasts. Game Over.")
    else:
      print("Wrong Input")

  elif action=="swim":
    print("You think you can swim in ocean but you Drowned. Game Over")
  else:
    print("Wrong Input")

elif dir=="right":
  print("Right is not always right. Game Over")
  
else:
  print("Wrong Input")