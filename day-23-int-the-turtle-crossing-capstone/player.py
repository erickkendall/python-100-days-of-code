from turtle import Turtle
from typing import Tuple

# Constants at the module level (good practice)
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    """Represents the player's turtle that needs to cross the road."""
    
    def __init__(self):
        """Initialize the player at the starting position facing upward."""
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.go_to_start()
        self.setheading(90)  # Face upward

    def go_up(self):
        """Move the turtle forward."""
        self.forward(MOVE_DISTANCE)

    def is_at_finish_line(self) -> bool:
        """Check if the turtle has reached the finish line.
        
        Returns:
            bool: True if turtle crossed the finish line, False otherwise.
        """
        return self.ycor() > FINISH_LINE_Y

    def go_to_start(self):
        """Move the turtle back to the starting position."""
        self.goto(STARTING_POSITION)
