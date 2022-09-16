import random
from random_word import RandomWords

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

logo = ''' 
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/    '''
                
print(logo)
end_of_game = False
r = RandomWords()
# Return a single random word
chosen_word = r.get_random_word()
word_length = len(chosen_word)

#TODO-1: - Create a variable called 'lives' to keep track of the number of lives left. 
#Set 'lives' to equal 6.

live = 6
print("You have total 6 lives.")

#Testing code
print(f'The word you have to guess has  {word_length} letters.')

#Create blanks
display = []
for _ in range(word_length):
    display += "_"

print(f"{' '.join(display)}")

print(stages[live])

while not end_of_game:
    guess = input("Guess a letter: ").lower()
    isGuess = False
    #Check guessed letter
    for position in range(word_length):
        letter = chosen_word[position]
        # print(f"Current position: {position}\n Current letter: {letter}\n Guessed letter: {guess}")
        if letter == guess:
            isGuess = True
            display[position] = letter
    if isGuess == True:
        print(f"You have already guessed the letter '{guess}'")
    else:
        print(f"You guessed '{guess}' which is a not in word. You Lose a live !")        

    #TODO-2: - If guess is not a letter in the chosen_word,
    #Then reduce 'lives' by 1.
    if isGuess == False and live > 0:
        live -= 1
        
      
      
    #If lives goes down to 0 then the game should stop and it should print "You lose."
    if live == 0 :
        print(" You Lose")
        print(f"Correct word was ' {chosen_word} '")
        end_of_game = True 

    #Join all the elements in the list and turn it into a String.
    print(f"{' '.join(display)}")

    #Check if user has got all letters.
    if "_" not in display:
        end_of_game = True
        print("You win.")

    #TODO-3: - print the ASCII art from 'stages' that corresponds to the current number of 'lives' 
    # the user has remaining.
    print(stages[live])
    
  
  
  