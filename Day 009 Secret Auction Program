#The purpose of this program is to practice with dictionaries, for loops, while loops,
#and defining functions. I also implemented screen clearing, and adding more comments
#to explain purpose of code. I do want to work on naming variables, as I often use names
#that are too similar.

#Define initial variables and import neccessary modules
import os
bids = {}

#Function to find highest bid with a parameter of a dictionary of bids.
def find_highest_bid(bidding_history):
    #Define additional variables
    high_bidder = ""
    high_bid = 0

    #Loop through all bidders, find the highest bid and the bidders name.
    for bidder in bidding_history:
        if bidding_history[bidder] > high_bid:
            high_bidder = bidder
            high_bid = bidding_history[bidder]
    return (high_bidder, high_bid)

def add_bids():
    #Define variables
    more_bids = True
    bidders = {}

    #Loop to continue adding more bidders and their bids.
    while more_bids:
        #Ask user their name, and change case so that their is proper capitalization.
        name = input("What is your name?: ").title()
        
        #Ask user for their bid amount. Validate that they enter a whole number.
        bid = input("What is your bid?: $")
        while not type(bid) == int:
            try:
                bid = int(bid)
            except:
                bid = input("Please enter your bid as a whole number: $")
        
        #Add the bidder and their bid to the dictionary "bidders".
        bidders[name] = bid

        #Ask user if there are other bidders. Validate that they type "yes" or "no".
        #If they type "no", break the while loop of more_bids.
        other_bidders = ""
        while not other_bidders == "yes" and not other_bidders == "no":
            other_bidders = input("Are there any other bidders? (yes/no): ").lower()
        if other_bidders == "no":
            more_bids = False
        
        #This will clear the screen using the appropriate command based on the operating system
        os.system("cls" if os.name == "nt" else "clear")
    return bidders

#Run the add_bids function.
print("Welcome to the secret auction program.")
bids = add_bids()

#Run the find_highest_bid function and print result to user.
winner, amount = find_highest_bid(bids)
print(f"The winner is {winner} with a bid of ${amount}.")
