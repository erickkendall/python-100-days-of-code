# Day 9 - Dictionaries, Nesting and the Secret Auction
# 100 Days of Code - Python Pro Bootcamp

from art import logo
bidder_data = {}

bidding_active = True

print(logo)

while bidding_active:
    bidder_name = input("What is the person's name? ")
    bid_amount = input("How much is your bid? ")

    bidder_data[bidder_name] = int(bid_amount)

    while True:
        continue_bidding = input("Any more bids? ").lower()
        if continue_bidding == "no":
            bidding_active = False
            break
        elif continue_bidding == "yes":
            break
        else:
            print("Please enter yes or no.")

highest_bid = 0
highest_bidder = ""  # Initialize this variable

for bidder, amount in bidder_data.items():
    if amount > highest_bid:
        highest_bid = amount
        highest_bidder = bidder

print(f"The winner is: {highest_bidder} with a bid of ${highest_bid}")
