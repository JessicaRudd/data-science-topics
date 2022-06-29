import os
from game_data import data
from art import logo, vs
import random

# Generate a random account from the game data.
def get_random_account():
    """ Get data from random account """
    return random.choice(data)

# Format account data into printable format.
def format_account(account):
    name = account["name"]
    # follower_count = account["follower_count"]
    description = account["description"]
    country = account["country"]

    return f"{name}, a {description}, from {country}."

# Check if user is correct.
def check_answer(user_guess, a_followers, b_followers):
    if a_followers > b_followers:
        return user_guess == "a"
    else:
        return user_guess == "b"

def game():
    print(logo)
    score = 0
    continue_game = True

    ## Get follower count.
    account_a = get_random_account()
    account_b = get_random_account()
    
    while continue_game:

        account_a = account_b
        account_b = get_random_account()

        while account_a == account_b:
            account_b = get_random_account()

        # Ask user for a guess.
        print(f"Compare A: {format_account(account_a)}.")
        print(vs)
        print(f"Against B: {format_account(account_b)}.")
        user_guess = input("Who has more followers? Type 'A' or 'B': ").lower()

        # Get follower counts
        a_followers = account_a["follower_count"]
        b_followers = account_b["follower_count"]

        is_correct = check_answer(user_guess, a_followers, b_followers)

        os.system("clear")
        print(logo)
        if is_correct:
            score +=1
            print(f"You're right! Current score {score}")
        else:
            continue_game = False
            print(f"Sorry, that's wrong! Final score: {score}")

game()




