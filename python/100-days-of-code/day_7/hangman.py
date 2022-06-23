# Step 1
from hangman_art import logo, stages
from hangman_words import word_list
import random
import os


print(logo)
end_of_game = False
lives = len(stages) - 1

# Randomly choose a word from the word_list and assign it to a variable called chosen_word.
chosen_word = random.choice(word_list)
word_length = len(chosen_word)

# Testing code
# print(f'Pssst, the solution is {chosen_word}.')

# Create an empty List called display.
#For each letter in the chosen_word, add a "_" to 'display'.
#So if the chosen_word was "apple", display should be ["_", "_", "_", "_", "_"] with 5 "_" representing each letter to guess.
display = []
for _ in range(word_length):
    display += "_"

# Use a while loop to let the user guess again. The loop should only stop once the user has guessed all the letters in the chosen_word and 'display' has no more blanks ("_"). Then you can tell the user they've won.
while not end_of_game:
    # Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.
    
    guess = (input("Guess a letter: ")).lower()
    
    # Clearing the screen between guesses 
    os.system('clear')
    if guess in display:
        print(f"You've already guessed letter: {guess}. Please choose a new letter.")

    for position, letter in enumerate(chosen_word):
        # print(f"Current position: {position}\n Current letter: {letter}\n Guessed letter: {guess}")
        if letter == guess:

            display[position] = letter
    
    #Join all the elements in the list and turn it into a String.   
    print(f"{' '.join(display)}")
    #TODO-2: - If guess is not a letter in the chosen_word,
    #Then reduce 'lives' by 1. 
    #If lives goes down to 0 then the game should stop and it should print "You lose."
    if guess not in chosen_word:
        print(f"{guess} is not in the word. You lose a life.")
        lives -= 1
    
        if lives == 0:
            end_of_game = True
            print("You lose!")
            print(f"The word was {chosen_word}")

    if "_" not in display:
        end_of_game = True
        print("You win!")

    #TODO-3: - print the ASCII art from 'stages' that corresponds to the current number of 'lives' the user has remaining.
    print(stages[lives])