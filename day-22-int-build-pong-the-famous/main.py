# Day 22 - Build Pong: The Famous Arcade Game
# 100 Days of Code - Python Pro Bootcamp

# Your code here
"""
Pong Game - Main Module
A classic Pong arcade game implementation using Python's turtle graphics.
"""
from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import ScoreBoard
from time import sleep


def setup_game():
    """Initialize and configure the game screen."""
    screen = Screen()
    screen.bgcolor("black")
    screen.setup(width=800, height=600)
    screen.title("Pong")
    screen.tracer(0)  # Turn off automatic screen updates
    return screen


def main():
    """Main game function that initializes components and runs the game loop."""
    # Setup the game window
    screen = setup_game()
    
    # Create game objects
    ball = Ball()
    scoreboard = ScoreBoard()
    right_paddle = Paddle((350, 0))
    left_paddle = Paddle((-350, 0))
    
    # Configure keyboard controls
    screen.listen()
    screen.onkey(right_paddle.go_up, "Up")
    screen.onkey(right_paddle.go_down, "Down")
    screen.onkey(left_paddle.go_up, "w")
    screen.onkey(left_paddle.go_down, "s")
    
    # Main game loop
    game_is_on = True
    while game_is_on:
        sleep(ball.move_speed)
        screen.update()
        ball.move()
        
        # Detect collision with top or bottom walls
        if ball.ycor() > 280 or ball.ycor() < -280:
            ball.bounce_y()
        
        # Detect collision with paddles
        if ((ball.distance(right_paddle) < 50 and ball.xcor() > 320) or 
                (ball.distance(left_paddle) < 50 and ball.xcor() < -320)):
            ball.bounce_x()
        
        # Detect when right paddle misses
        if ball.xcor() > 380:
            scoreboard.left_point()
            ball.reset_position()
        
        # Detect when left paddle misses
        if ball.xcor() < -380:
            scoreboard.right_point()
            ball.reset_position()
    
    screen.exitonclick()


if __name__ == "__main__":
    main()
