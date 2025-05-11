from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")


class ScoreBoard(Turtle):
    """A class to create and manage the score display in the snake game."""
    
    def __init__(self, score=0):
        """Initialize the scoreboard with a starting score."""
        super().__init__()
        self.score = score
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.display_score()

    def increase_score(self):
        """Increment the score by 1."""
        self.score += 1

    def game_over(self):
        """Display 'GAME OVER' text in the center of the screen."""
        self.home()
        self.write("GAME OVER", align=ALIGNMENT, font=FONT)

    def display_score(self):
        """Update and display the current score."""
        self.clear()
        self.write(f"Score: {self.score}", False, align=ALIGNMENT, font=FONT)
