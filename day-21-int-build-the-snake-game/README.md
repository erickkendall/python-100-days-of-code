# Snake Game

A classic arcade-style snake game implemented in Python using the Turtle graphics library. Navigate the snake to eat food while avoiding walls and your own tail.

## Description

This Snake Game implementation uses Python's Turtle module to create a visually engaging version of the classic arcade game. Players control a snake that grows longer each time it consumes food. The challenge is to grow as long as possible without colliding with the walls or the snake's own body.

The game features:
- Smooth snake movement with directional controls
- Randomly appearing food
- Score tracking
- Game over detection
- Simple, clean visuals

## Game Components

The project consists of four Python files:
1. `main.py` - Contains the game loop and ties all components together
2. `snake.py` - Defines the Snake class that handles the snake's behavior
3. `food.py` - Implements the Food class for generating food items
4. `scoreboard.py` - Manages score display and game over messages

## How to Play

1. Ensure you have Python 3 installed on your system.
2. Make sure the Turtle graphics library is available (included in standard Python installations).
3. Download all four files (`main.py`, `snake.py`, `food.py`, and `scoreboard.py`) into the same directory.
4. Run the game from your terminal/command prompt:
   ```
   python main.py
   ```
5. Control the snake using the arrow keys:
   - Up arrow: Move up
   - Down arrow: Move down
   - Left arrow: Move left
   - Right arrow: Move right
6. The game ends when the snake hits a wall or collides with its own body.
7. Your score increases each time the snake eats food.

## Game Rules

- The snake moves continuously in the current direction
- Each time the snake eats food, it grows longer and your score increases
- The snake cannot reverse direction (e.g., if moving right, you cannot immediately go left)
- The game ends when the snake hits the wall or collides with itself

## Features and Logic

- **Snake Movement**: The snake's body follows its head by having each segment move to the position of the segment ahead of it.
- **Food Generation**: Food appears randomly on the screen after being eaten.
- **Collision Detection**:
  - Checks for collision with food
  - Checks for collision with walls
  - Checks for collision with the snake's own body
- **Score System**: Keeps track of the player's score as they eat more food.
- **Game Over**: Displays a game over message when the player loses.

## Code Structure

- `main.py`:
  - Sets up the game window
  - Handles the game loop
  - Manages collision detection
  - Coordinates game components
- `snake.py`:
  - Creates and manages the snake object
  - Handles snake movement and growth
  - Implements directional controls
- `food.py`:
  - Creates the food object
  - Manages random repositioning when food is eaten
- `scoreboard.py`:
  - Displays the current score
  - Shows the game over message

## Customization

You can customize the game by:
- Adjusting the screen size in `main.py`
- Changing the snake's speed by modifying the `sleep()` time in the game loop
- Altering the snake's appearance by editing the shape, color, or size in `snake.py`
- Modifying the food appearance in `food.py`
- Changing the score position or font in `scoreboard.py`

## Possible Enhancements

- Implement a high score system
- Add different levels with increasing difficulty
- Include obstacles on the play field
- Create power-ups with special effects
- Add a restart option after game over
- Implement boundary wrapping (snake appears on opposite side when hitting a wall)

## Credits

This project is part of the "100 Days of Code - Python Pro Bootcamp" curriculum.

## License

This project is open source and available under the [MIT License](https://opensource.org/licenses/MIT).
