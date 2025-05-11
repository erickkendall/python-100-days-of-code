from turtle import Turtle
from random import randint


class Food(Turtle):
    """A class to create and manage food for the snake game.
    
    The food appears as a small blue circle at random positions on the screen.
    """
    def __init__(self):
        """Initialize the food object with visual properties and position."""
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("blue")
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        """Move the food to a new random position on the screen."""
        random_x = randint(-280, 280)
        random_y = randint(-280, 280)
        self.goto(random_x, random_y)
