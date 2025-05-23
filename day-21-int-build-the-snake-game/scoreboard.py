from turtle import Turtle
import os

ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")


class ScoreBoard(Turtle):
    """A class to create and manage the score display in the snake game."""
    
    def __init__(self, score=0):
        """Initialize the scoreboard with a starting score."""
        super().__init__()
        self.score = score
        with open("data.txt", "r") as data:
            self.high_score=int(data.read())

        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score}" f"High Score: {self.high_score}", False, align=ALIGNMENT, font=FONT)

    def increase_score(self):
        """Increment the score by 1."""
        self.score += 1
        self.update_scoreboard()

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", "w") as data:
                data.write(f"{self.high_score}")
        self.score = 0
        self.update_scoreboard()

