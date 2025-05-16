# Turtle Crossing Game

A challenging arcade-style game where players must guide a turtle across a busy road without getting hit by cars.

## Description

This Turtle Crossing game is a Python implementation of the classic road-crossing arcade concept. Players control a turtle that must safely navigate from the bottom of the screen to the top while avoiding randomly generated cars moving at increasing speeds. Each successful crossing levels up the game, making the cars move faster.

The game features:
- Colorful cars with random colors and positions
- Progressively increasing difficulty with each level
- Visual level tracking
- Simple up-arrow key controls
- Game over screen when collision occurs

## Game Components

The project consists of four Python files:
1. `main.py` - The primary game loop and initialization
2. `player.py` - Controls the turtle character and movement
3. `car_manager.py` - Manages car creation, movement, and speed
4. `scoreboard.py` - Handles level display and game over message

## How to Play

1. Ensure you have Python 3 installed on your system.
2. Make sure the `turtle` module is available (included in standard Python).
3. Download all four files (`main.py`, `player.py`, `car_manager.py`, and `scoreboard.py`) into the same directory.
4. Run the game from your terminal/command prompt:
   ```
   python main.py
   ```
5. The game will:
   - Display a blank screen with a turtle at the bottom
   - Show the current level in the top-left corner
   - Generate random cars moving from right to left
6. Controls:
   - Press the **Up Arrow** key to move the turtle forward
7. The game ends when either:
   - Your turtle collides with a car (lose)
   - You can continue playing and leveling up indefinitely by successfully crossing

## Example Gameplay

When you start the game, you'll see:
- A turtle at the bottom of the screen
- "Level: 1" displayed in the top-left corner
- Colorful cars (red, orange, yellow, green, blue, purple) moving from right to left

As you successfully cross to the top:
- Your turtle returns to the starting position
- The level counter increases
- Cars move faster, making the game more challenging

If you collide with a car:
- "GAME OVER" appears in the center of the screen
- The game stops
- Click anywhere on the screen to exit

## Features and Logic

- **Player Movement**: The turtle moves upward in response to the Up Arrow key.
- **Car Generation**: Cars are randomly generated on the right side of the screen with:
  - Random Y-positions
  - Random colors (from a predefined list)
  - 1/6 probability of creation on each game cycle
- **Collision Detection**: The game detects when the turtle gets too close to any car.
- **Level System**: 
  - Each successful crossing increases the level
  - Car speed increases with each level
  - Level is displayed on screen
- **Visual Feedback**:
  - Clear "GAME OVER" message when losing
  - Level indicator updates with progress

## Code Structure

- `main.py`:
  - Sets up the game screen and objects
  - Contains the main game loop
  - Handles collision detection and level-up logic
- `player.py`:
  - Defines the Player class
  - Controls turtle movement and position
  - Detects when the finish line is reached
- `car_manager.py`:
  - Manages car creation with random attributes
  - Controls car movement speed
  - Handles speed increases for level progression
- `scoreboard.py`:
  - Displays and updates the current level
  - Shows the game over message when needed

## Customization

You can customize the game by:
- Adjusting the `STARTING_MOVE_DISTANCE` and `MOVE_INCREMENT` in `car_manager.py` to change difficulty
- Modifying the `COLORS` list in `car_manager.py` to change car colors
- Changing the `MOVE_DISTANCE` in `player.py` to alter how far the turtle moves with each key press
- Updating the `FONT` in `scoreboard.py` to change text appearance

## Credits

This project is part of the "100 Days of Code - Python Pro Bootcamp" curriculum (Day 23 - The Turtle Crossing Capstone Project).

## License

This project is open source and available under the [MIT License](https://opensource.org/licenses/MIT).
