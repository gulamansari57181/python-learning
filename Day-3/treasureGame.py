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
direction = input("You are at crossroad. Where do you want to go ? Type 'left' or 'right':\n").lower()

if direction !='left':
    print(" Oops!! You fall into a hole. Game Over")
    exit()
lakeChoice = input("You come to a lake. There is an Island in the middle of the lake. Type 'wait'to wait for a boat or 'swim' to swim across.\n").lower()

if lakeChoice !='wait':
    print("You have been attacked by trout. Game over. Better luck next time !")
    exit()
color = input("You arrive at the Islan unharmed. There is a house with 3 doors. One red, one yellow, one blue. Which color do you choose ?\n")

if color =='red':
    print("Ohhh No! You are burned with fire. Game Over. Hard Luck.")

elif color =='yellow':
    print("Hurray!!! You are the saviour. Congratulations")
    
elif color=='blue':
    print("Ohh no ! You are eaten by beasts game over !")
else:
    print("You chose a door that doesn't exist. Game Over!!!!")
              