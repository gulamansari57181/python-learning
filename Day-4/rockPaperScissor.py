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
---'   ____)_______
          _________)
       __________)
      (____)
---.__(___)
'''

choice = int(input("What do you want to choose ?\n1 -> for rock\n2 -> for Paper\n3 -> for Scissors\n"))

choice_list=['rock','paper','scissors']
user_choice=choice_list[choice-1]

# Generating random computer choice
computer_choice=choice_list[random.randint(1,3)-1]

# If user chose -> rock
if user_choice=='rock':
    if computer_choice=='scissors':
        print(f"You chose rock: {rock}")
        print(f"Computer chose scissors: {scissors}")
        print("Hurray You Won")
    elif computer_choice=='paper':
        print(f"You chose rock: {rock}")
        print(f"Computer chose paper: {paper}")
        print("You lose. Better luck next time.")
    else:
         print(f"You chose rock: {rock}")
         print(f"Computer also  chose rock: {rock}")
         print("Game Draw. You guys are same. ")

# if user chose paper ->
elif user_choice=='paper':
    if computer_choice=='scissors':
        print(f"You chose paper: {paper}")
        print(f"Computer chose scissors: {scissors}")
        print("You lose. Better luck next time.")
    elif computer_choice=='paper':
        print(f"You chose paper: {paper}")
        print(f"Computer chose paper: {paper}")
        print("Game Draw. You guys are same. ")
    else:
         print(f"You chose paper: {paper}")
         print(f"Computer  chose rock: {rock}")
         print("Hurray You Won") 
# if user chose -> scissors
else:
      if computer_choice=='scissors':
        print(f"You chose scissors: {scissors}")
        print(f"Computer chose scissors: {scissors}")
        print("Game Draw. You guys are same. ")
      elif computer_choice=='paper':
        print(f"You chose scissors: {scissors}")
        print(f"Computer chose paper: {paper}")
        print("Hurray You Won") 
      else:
        print(f"You chose scissors: {scissors}")
        print(f"Computer  chose rock: {rock}")
        print("You lose. Better luck next time.")
    