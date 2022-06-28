#Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).
from art import logo
from random import randint
import os

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5

def check_answer(guess, answer, turns):
    """ Checks answer against guess. Returns the number of turns remaining. """
    if guess > answer:
        print("Too high.")
        return turns - 1

    elif guess < answer:
        print("Too low.")
        return turns - 1

    else:
        print(f"You win! The correct number was {answer}")

def set_difficulty():

    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
    
    if difficulty == "hard":
        return HARD_LEVEL_TURNS
    else:
        return EASY_LEVEL_TURNS


def guessing_game():


    print(logo)
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    computer_number = randint(1, 100)
    turns = set_difficulty()

    player_guess = 0

    while player_guess != computer_number:
        print(f"You have {turns} attempts remaining to guess the number.")

        #Guess a number
        player_guess = int(input("Guess a number: "))

        # Track turns and reduce by 1 if player guesses wrong.
        turns = check_answer(player_guess, computer_number, turns)

        if turns == 0:
            print(f"You ran out of guesses. The correct number was {computer_number} ")
            return
        elif player_guess != computer_number:
            print("Guess again!")
            
keep_playing = True

while keep_playing:
    guessing_game()
    play_again = input("Would you like to play again? Type 'y' or 'n'. ")
    if play_again == "n":
        keep_playing = False
    os.system("clear")
