# Day 23 - The Turtle Crossing Capstone Project
# 100 Days of Code - Python Pro Bootcamp

# Your code here
#!/usr/bin/env python3
"""
Turtle Crossing Game - The player must guide a turtle across a busy road without getting hit by cars.
Day 23 - 100 Days of Code - Python Pro Bootcamp
"""

import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard


def main():
    """Run the main game loop."""
    screen = Screen()
    screen.setup(width=600, height=600)
    screen.tracer(0)
    
    player = Player()
    car_manager = CarManager()
    scoreboard = Scoreboard()

    screen.listen()
    screen.onkey(player.go_up, "Up")

    game_is_on = True
    while game_is_on:
        time.sleep(0.1)
        screen.update()

        car_manager.create_car()
        car_manager.move_cars()

        # Detect collision with car
        for car in car_manager.all_cars:
            if car.distance(player) < 20:
                game_is_on = False
                scoreboard.game_over()

        # Detect successful crossing
        if player.is_at_finish_line():
            player.go_to_start()
            car_manager.level_up()
            scoreboard.increase_level()  # This was missing!

    screen.exitonclick()


if __name__ == "__main__":
    main()
