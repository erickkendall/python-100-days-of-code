# Pong Game

A classic arcade game recreation where two players control paddles to hit a ball back and forth across the screen.

## Description

This Pong implementation is a graphical game built with Python's Turtle graphics module. Players control paddles on either side of the screen, aiming to hit the ball past their opponent's paddle to score points. The game features increasing difficulty as the ball speeds up after each successful hit.

The game features:
- Two-player gameplay with keyboard controls
- Dynamic ball movement with increasing speed
- Score tracking for both players
- Simple collision detection system
- Clean, black and white retro aesthetic

## Game Components

The project consists of four Python files:
1. `main.py` - The main game loop and setup
2. `paddle.py` - Contains the Paddle class for player-controlled paddles
3. `ball.py` - Contains the Ball class with movement and collision mechanics
4. `scoreboard.py` - Contains the ScoreBoard class for tracking player scores

## How to Play

1. Ensure you have Python 3 installed on your system with the turtle module (included in standard library).
2. Download all four files (`main.py`, `paddle.py`, `ball.py`, and `scoreboard.py`) into the same directory.
3. Run the game from your terminal/command prompt:
   ```
   python main.py
   ```
4. The game controls are:
   - Right paddle: Up and Down arrow keys
   - Left paddle: 'W' (up) and 'S' (down) keys
5. Each time a player misses the ball, the opponent scores a point.
6. The ball speeds up after each successful hit, making the game progressively challenging.
7. To exit the game, click on the game window.

## Example Gameplay

When you start the game, you'll see a black screen with:
- Two white paddles on the left and right sides
- A white ball in the center
- Score display at the top of the screen

As you play:
- The ball moves across the screen
- Players move their paddles up and down to intercept the ball
- When the ball hits a paddle, it bounces back with increased speed
- When a player misses, the opponent scores a point
- After a point is scored, the ball resets to the center

## Features and Logic

- **Paddle Movement**: Simple up and down controls for each player's paddle.
- **Ball Physics**: 
  - The ball bounces off the top and bottom walls
  - When hitting a paddle, the ball reverses direction and increases speed
  - After a point is scored, the ball resets position and speed
- **Scoring System**: Tracks points for both players and updates the displayed score.
- **Game Loop**: The main loop handles all game events including movement, collisions, and scoring.

## Code Structure

- `main.py`:
  - Sets up the game screen
  - Creates game objects
  - Contains the main game loop
  - Manages collision detection and scoring
- `paddle.py`:
  - Defines the Paddle class for player-controlled paddles
  - Handles paddle movement methods
- `ball.py`:
  - Defines the Ball class with movement mechanics
  - Manages ball speed, direction, and reset functionality
- `scoreboard.py`:
  - Manages and displays the score for both players

## Customization

You can customize the game by:
- Changing paddle sizes in the `paddle.py` file
- Adjusting the ball speed or acceleration in `ball.py`
- Modifying the screen dimensions in `main.py`
- Changing the controls by editing key bindings in `main.py`

## Educational Value

This project demonstrates:
- Object-oriented programming principles
- Game loop architecture
- Basic physics simulation
- Event-driven programming
- User input handling
- Graphics programming with Python's Turtle module

## Requirements

- Python 3.x
- No additional packages required (uses standard library only)

## Credits

This project is part of the "100 Days of Code - Python Pro Bootcamp" curriculum.

## License

This project is open source and available under the [MIT License](https://opensource.org/licenses/MIT).
