# Day 11 - The Blackjack Capstone Project
# 100 Days of Code - Python Pro Bootcamp

# Your code here
import random

def deal_cards():
    """Returns a random card from the deck."""
    cards = []
    values = ('A 1 2 3 4 5 6 7 9 10 J Q K')
    cards = values.split(' ')
    
    dealt = random.choice(cards)
    print(dealt)
    if dealt.isdigit():
        dealt = int(dealt)
    elif dealt == "A":
        dealt = 11
    else:
        dealt = 10
    
    return dealt    

user_cards = []
computer_cards = []

for _ in range(2):
    user_cards.append(deal_cards())
    computer_cards.append(deal_cards())

user_sum = sum(user_cards)
computer_sum = sum(computer_cards)

