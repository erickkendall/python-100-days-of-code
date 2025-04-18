# Day 4 - Randomisation and Python Lists
# 100 Days of Code - Python Pro Bootcamp

# Your code here
import random


rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

def output(val):
    if val == "rock":
        print(rock)
    elif val == "paper":
        print(paper)
    else:
        print(scissors)


hand_positions = ["rock", "paper", "scissors"]
user_choice = input(f"Choose one: {', '.join(hand_positions)}: ")
if user_choice not in hand_positions:
    print("That's not a valid choice. Try again.")
else:
    output(user_choice)
    print(f"User picks {user_choice}.")

    computer_choice = random.choice(hand_positions)
    output(computer_choice)
    print(f"COMPUTER picks {computer_choice}.")



    if computer_choice == "rock" and user_choice == "scissors":
        print("Rock smashes scissors. COMPUTER wins.")
    elif computer_choice == "scissors" and user_choice == "rock":
        print("Rock smashes scissors. User wins.")
    elif computer_choice == "paper" and user_choice == "rock":
        print("Paper covers rock. COMPUTER wins.")
    elif computer_choice == "rock" and user_choice == "paper":
        print("Paper covers rock. User wins.")
    elif computer_choice == "scissors" and user_choice == "paper":
        print("Scissors cuts paper, COMPUTER wins.")
    elif computer_choice == "paper" and user_choice == "scissors":
        print("Scissors cuts paper, User wins.")
    else:
        print("Tie!")

