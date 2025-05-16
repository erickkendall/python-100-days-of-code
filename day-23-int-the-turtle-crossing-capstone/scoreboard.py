from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    """Displays and manages the game score and level information."""
    
    def __init__(self):
        """Initialize the scoreboard at the top left corner."""
        super().__init__()
        self.level = 1
        self.hideturtle()
        self.penup()
        self.goto(-280, 260)
        self.update_scoreboard()

    def update_scoreboard(self):
        """Update the display with the current level."""
        self.clear()
        self.write(f"Level: {self.level}", align="left", font=FONT)

    def increase_level(self):
        """Increment the level and update the display."""
        self.level += 1
        self.update_scoreboard()

    def game_over(self):
        """Display game over message in the center of the screen."""
        self.home()  # Move to center
        self.write("GAME OVER", align="center", font=FONT)
