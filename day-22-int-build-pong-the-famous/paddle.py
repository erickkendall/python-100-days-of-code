"""
Paddle Module for Pong Game
Defines the Paddle class that players control.
"""
from turtle import Turtle


class Paddle(Turtle):
    """
    Paddle class representing a player-controlled paddle.
    
    Inherits from Turtle class and provides methods for paddle movement.
    """
    
    def __init__(self, position):
        """
        Initialize a new paddle.
        
        Args:
            position (tuple): The (x, y) coordinates for paddle position
        """
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)  # 5x1 rectangle
        self.penup()
        self.goto(position)
    
    def go_up(self):
        """Move the paddle upward by 20 pixels."""
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)
    
    def go_down(self):
        """Move the paddle downward by 20 pixels."""
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)
