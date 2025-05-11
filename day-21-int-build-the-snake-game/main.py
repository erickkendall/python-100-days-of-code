# Day 21 - Build the Snake Game Part 2: Inheritance & List Slicing
# 100 Days of Code - Python Pro Bootcamp

# Your code here
"""
Snake Game
A classic snake game implementation using Python's turtle module.
Part of the 100 Days of Code - Python Pro Bootcamp
"""

from turtle import Screen
from time import sleep
from snake import Snake
from food import Food
from scoreboard import ScoreBoard


def main():
    """Initialize and run the snake game."""
    # Set up the screen
    screen = Screen()
    screen.setup(width=600, height=600)
    screen.bgcolor("black")
    screen.title("Snake Game")
    screen.tracer(0)  # Turn off animation updates

    # Create game objects
    snake = Snake()
    food = Food()
    score = 0
    scoreboard = ScoreBoard(score)

    # Set up key listeners
    screen.listen()
    screen.onkey(snake.up, "Up")
    screen.onkey(snake.down, "Down")
    screen.onkey(snake.left, "Left")
    screen.onkey(snake.right, "Right")

    # Main game loop
    game_is_on = True
    
    while game_is_on:
        screen.update()  # Manual screen update
        sleep(0.1)  # Control game speed
        
        snake.move()
      
        # Detect collision with food
        if snake.head.distance(food) < 15:
            food.refresh()
            snake.extend()
            scoreboard.increase_score()
            scoreboard.display_score()

        # Detect collision with wall
        if (snake.head.xcor() > 280 or snake.head.xcor() < -280 or 
            snake.head.ycor() > 280 or snake.head.ycor() < -280):
            scoreboard.game_over()
            game_is_on = False

        # Detect collision with own tail
        for segment in snake.segments[1:]:
            if snake.head.distance(segment) < 10:
                scoreboard.game_over()
                game_is_on = False

    # Close the game window on click
    screen.exitonclick()


if __name__ == "__main__":
    main()
