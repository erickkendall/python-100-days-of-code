"""
Ball Module for Pong Game
Defines the Ball class with movement and bounce mechanics.
"""
from turtle import Turtle


class Ball(Turtle):
    """
    Ball class representing the game ball.
    
    Inherits from Turtle class and provides methods for ball movement and collision.
    """
    
    def __init__(self):
        """Initialize a new ball with default properties."""
        super().__init__()
        self.color("white")
        self.shape("circle")
        self.penup()
        self.x_move = 10  # Initial horizontal movement amount
        self.y_move = 10  # Initial vertical movement amount
        self.move_speed = 0.1  # Controls game speed
    
    def move(self):
        """Move the ball based on current movement values."""
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)
    
    def bounce_y(self):
        """Reverse the vertical direction of the ball."""
        self.y_move *= -1
    
    def bounce_x(self):
        """
        Reverse the horizontal direction of the ball and increase speed.
        Called when the ball hits a paddle.
        """
        self.x_move *= -1
        self.move_speed *= 0.9  # Make the ball move faster
    
    def reset_position(self):
        """Reset the ball to the center and reset speed."""
        self.goto(0, 0)
        self.move_speed = 0.1
        self.bounce_x()  # Change direction when resetting
