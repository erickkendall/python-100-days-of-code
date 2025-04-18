# Day 14 - Higher Lower Game Project
# 100 Days of Code - Python Pro Bootcamp

from random import randint
from game_data import data
from art import logo, vs

def get_random_celebrity():
    '''Return a celebrity_a from the list of celebrities.'''
    return data[randint(0, len(data)-1)]

celebrity_a = get_random_celebrity()
celebrity_b = get_random_celebrity()

score = 0
game_over = False

print(logo)
while not game_over:

    while celebrity_a == celebrity_b:
        celebrity_b = get_random_celebrity()         

    if celebrity_a['follower_count'] == celebrity_b['follower_count']:
        celebrity_b = get_random_celebrity()

    # Display the celebrities
    print(f"Compare A: {celebrity_a['name']}, a {celebrity_a['description']} from {celebrity_a['country']}")
    print(vs)
    print(f"Against B: {celebrity_b['name']}, a {celebrity_b['description']} from {celebrity_b['country']}")

    if celebrity_a['follower_count'] > celebrity_b['follower_count']:
        correct_answer = 'A'
    
    elif celebrity_a['follower_count'] < celebrity_b['follower_count']:
        correct_answer = 'B'
        
    guess = input("Who has more followers? Type 'A' or 'B': ").upper()

    if guess == correct_answer:
        score += 1
        print(f"You're right! Current score: {score}")

        if correct_answer == 'B':
            celebrity_a = celebrity_b

        celebrity_b = get_random_celebrity()
    else:
        game_over = True
        print(f"Sorry, that's wrong. Final score: {score}")
