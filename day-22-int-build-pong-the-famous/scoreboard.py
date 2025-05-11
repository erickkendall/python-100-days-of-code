"""
Scoreboard Module for Pong Game
Defines the ScoreBoard class for tracking and displaying player scores.
"""
from turtle import Turtle


class ScoreBoard(Turtle):
    """
    ScoreBoard class for tracking and displaying player scores.
    
    Inherits from Turtle class and provides methods for score management.
    """
    
    def __init__(self):
        """Initialize the scoreboard with default scores of 0."""
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()  # Hide the turtle icon
        
        # Initialize scores
        self.left_score = 0
        self.right_score = 0
        
        # Display initial scores
        self.update_scoreboard()
    
    def update_scoreboard(self):
        """Clear and redraw the scoreboard with current scores."""
        self.clear()
        
        # Draw left player score
        self.goto(-100, 200)
        self.write(self.left_score, align="center", font=("Courier", 80, "normal"))
        
        # Draw right player score
        self.goto(100, 200)
        self.write(self.right_score, align="center", font=("Courier", 80, "normal"))
    
    def left_point(self):
        """Increment left player's score and update display."""
        self.left_score += 1
        self.update_scoreboard()
    
    def right_point(self):
        """Increment right player's score and update display."""
        self.right_score += 1
        self.update_scoreboard()
