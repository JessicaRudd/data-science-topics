from multiprocessing.connection import wait
import os
from art import logo

print(logo)

# Clearing the screen between guesses 
# os.system('clear')
add_bids = True
bid_dictionary = {}

def find_highest_bidder(bidding_record):
    highest_bid = 0
    winner = ""
    for bidder in bidding_record:
        bid_amount = bidding_record[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"The winner is {winner} with a bid of ${highest_bid}")
        

while add_bids == True:
    name = input("What is your name? ")
    bid = int(input("What is your bid? "))

    bid_dictionary[name] = bid

    more_bids = input("Are there other users who want to bid? Enter 'yes' or 'no'. ")

    if more_bids == "no":

        add_bids = False
        find_highest_bidder(bid_dictionary)
        # max_bid = max(bid_dictionary.values())
        # winner = max(bid_dictionary, key=bid_dictionary.get)
        # print(f"{winner} is the winner with a bid of ${max_bid}.")
        
    elif more_bids == "yes":
        os.system('clear')
