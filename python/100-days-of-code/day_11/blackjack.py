import random
import os
from art import logo

############### Blackjack Project #####################

#Difficulty Normal 😎: Use all Hints below to complete the project.
#Difficulty Hard 🤔: Use only Hints 1, 2, 3 to complete the project.
#Difficulty Extra Hard 😭: Only use Hints 1 & 2 to complete the project.
#Difficulty Expert 🤯: Only use Hint 1 to complete the project.

############### Our Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

##################### Hints #####################

#Hint 1: Go to this website and try out the Blackjack game: 
#   https://games.washingtonpost.com/games/blackjack/
#Then try out the completed Blackjack project here: 
#   http://blackjack-final.appbrewery.repl.run

#Hint 2: Read this breakdown of program requirements: 
#   http://listmoz.com/view/6h34DJpvJBFVRlZfJvxF
#Then try to create your own flowchart for the program.

#Hint 3: Download and read this flow chart I've created: 
#   https://drive.google.com/uc?export=download&id=1rDkiHCrhaf9eX7u7yjM1qwSuyEk-rPnt

def deal_card():
    """Returns a random card from the deck."""
    cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]
    card = random.choice(cards)
    return card

def calculate_score(card_hand_list):
    """Take a list of cards and return the score calculated from the cards"""

    if sum(card_hand_list) == 21 and len(card_hand_list) == 2:
        return 0

    if sum(card_hand_list) > 21 and 11 in card_hand_list:
        card_hand_list.remove(11)
        card_hand_list.append(1)

    return sum(card_hand_list)

def compare(user_score, computer_score):

    if user_score > 21 and computer_score > 21:
        return "You went over. You lose 😤"

    if user_score == computer_score:
        return "It's a draw! 🙃" 

    elif computer_score == 0:
        return "Computer has blackjack. You lose! 😱"
    
    elif user_score == 0:
        return "Blackjack! You win! 😎"

    elif user_score > 21:
        return "Bust! You lose! 😭"

    elif computer_score > 21:
        return "Computer busts! You win! 😁"

    elif user_score > computer_score:
        return "You win! 😃"
    else:
        return "You lose! 😤"

def play_game():
    
    print(logo)

    user_cards = []
    computer_cards = []
    game_over = False

    # Deal the user and computer cards
    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    while not game_over:

        # Calculate score
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        print(f" Your cards: {user_cards}, current score {user_score}")
        print(f" Computer first card: {computer_cards[0]}")

        if user_score == 0 or computer_score == 0 or user_score > 21:
            game_over = True
       
        else:
            hit = input("Type 'y' to get another card, type 'n' to pass: ")

            if hit == 'y':
                user_cards.append(deal_card())
            elif hit == 'no':
                game_over = True
        
    while computer_score < 17 and computer_score != 0:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

    print(f"   Your final hand: {user_cards}, final score: {user_score}")
    print(f"   Computer's final hand: {computer_cards}, final score: {computer_score}")
    print(compare(user_score, computer_score))

while input("Do you want to play a game of Blackjack? Type 'y' or 'no': ") == "y":
    os.system("clear")
    play_game()
