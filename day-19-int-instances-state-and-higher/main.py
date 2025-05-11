# Day 19 - Instances, State and Higher Order Functions
# 100 Days of Code - Python Pro Bootcamp

# Your code here
# Import necessary libraries
from turtle import Turtle, Screen
from random import choice, randint

# Set up the screen
screen = Screen()
screen.setup(width=500, height=400)  # Define screen dimensions

# Get user's bet
user_bet = screen.textinput(title="Make your bet!", prompt="Which turtle will win the race? Enter a color: ")
print(f"You bet on: {user_bet}")

# Define colors for turtles
colors = ["red", "orange", "yellow", "green", "blue", "purple"]

# Define race parameters
x_start = -230  # Starting x position
y_start = -100  # Starting y position for lowest turtle
finish_line = 100  # x coordinate of finish line

# Create dictionary to store turtle objects
racing_turtles = {}

# Initialize turtles and position them at the starting line
for color in colors:
    # Create a new turtle with the current color
    racing_turtles[color] = Turtle(shape="turtle")
    racing_turtles[color].color(color)
    racing_turtles[color].penup()
    racing_turtles[color].goto(x_start, y_start)
    y_start += 50  # Space turtles vertically
    
# Run the race
winner = None

while winner is None:
    # Reset colors list if empty
    if not colors:  # More Pythonic than checking len(colors) == 0
        colors = ["red", "orange", "yellow", "green", "blue", "purple"]
    
    # Choose a random turtle to move
    random_color = choice(colors)
    
    # Get current position of the selected turtle
    x, y = racing_turtles[random_color].pos()
    
    # Check if this turtle has crossed the finish line
    if x >= finish_line:
        winner = random_color
        break
    
    # Move the turtle forward by a random amount
    racing_turtles[random_color].forward(randint(1, 10))
    
    # Remove this color from the list so each turtle moves once per round
    colors.remove(random_color) 

# Announce the winner
print(f"The {winner} turtle won!")

# Show if user won their bet
if user_bet.lower() == winner.lower():
    print("You won your bet!")
else:
    print("Sorry, you lost your bet.")

# Keep window open until clicked
screen.exitonclick()
