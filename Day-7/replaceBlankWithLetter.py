#Step 2

import random
word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)

#Testing code
print(f'Pssst, the solution is {chosen_word}.')

#TODO-1: - Create an empty List called display.
#For each letter in the chosen_word, add a "_" to 'display'.
#So if the chosen_word was "apple", display should be ["_", "_", "_", "_", "_"] with 5 "_" representing each letter to guess.
display = []

for letter in chosen_word:
    display.append("_")

print(display)

#TODO-2: - Continue untill user guess all the letters correctly

while "_" in display: 
  guess = input("Guess a letter: ").lower() 
  for i in range(len(chosen_word)):
        if chosen_word[i] == guess:
         display[i]=guess
        
  print(display)  

print("You won !!")     
    





