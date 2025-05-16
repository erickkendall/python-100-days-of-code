from turtle import Turtle
from random import choice, randint
from typing import List  # Add type hints

# Constants are well-defined (good practice)
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    """Manages the creation and movement of cars."""
    
    def __init__(self):
        """Initialize the car manager with an empty list of cars and starting speed."""
        self.all_cars: List[Turtle] = []
        self.car_speed = STARTING_MOVE_DISTANCE

    def create_car(self):
        """Create a new car with a 1/6 probability."""
        random_chance = randint(1, 6)
        if random_chance == 1:
            new_car = Turtle("square")
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.penup()
            new_car.color(choice(COLORS))
            random_y = randint(-250, 250)
            new_car.goto(300, random_y)
            self.all_cars.append(new_car)

    def move_cars(self):
        """Move all cars from right to left."""
        for car in self.all_cars:
            car.backward(self.car_speed)

    def level_up(self):
        """Increase the speed of cars."""
        self.car_speed += MOVE_INCREMENT
