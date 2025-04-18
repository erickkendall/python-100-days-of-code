# Higher Lower Game

A fun command-line game where you guess which celebrity has more Instagram followers!

## Description

The Higher Lower Game is a Python-based guessing game where players are presented with two celebrities/brands and must guess which one has more Instagram followers. With each correct guess, your score increases by one point. The game continues until you make an incorrect guess.

## Features

- Simple command-line interface with ASCII art
- Database of 50+ celebrities and brands with their follower counts
- Score tracking system
- Randomly generated matchups for endless gameplay

## Installation

1. Make sure you have Python 3.x installed on your system
2. Clone or download this repository
3. Navigate to the project directory

## Files in the Project

- `main.py` - The main game logic
- `game_data.py` - Contains the database of celebrities and their follower counts
- `art.py` - ASCII art for the game interface

## How to Play

1. Run the game with `python main.py`
2. You'll be presented with two celebrities/brands (A and B)
3. Type 'A' or 'B' to guess which has more followers
4. If you're correct, your score increases and you continue playing
5. If you're wrong, the game ends and displays your final score

## Game Rules

- Each correct guess earns you 1 point
- The game continues until you make an incorrect guess
- If you correctly guess the higher one, that celebrity/brand becomes option A in the next round
- A new celebrity/brand is always generated for option B

## Sample Game

```
    __  ___       __             
   / / / (_)___ _/ /_  ___  _____
  / /_/ / / __ `/ __ \/ _ \/ ___/
 / __  / / /_/ / / / /  __/ /    
/_/ ///_/\__, /_/ /_/\___/_/     
   / /  /____/_      _____  _____
  / /   / __ \ | /| / / _ \/ ___/
 / /___/ /_/ / |/ |/ /  __/ /    
/_____/\____/|__/|__/\___/_/     

Compare A: Instagram, a Social media platform from United States
 _    __    
| |  / /____
| | / / ___/
| |/ (__  ) 
|___/____(_)

Against B: Cristiano Ronaldo, a Footballer from Portugal
Who has more followers? Type 'A' or 'B': A
You're right! Current score: 1
```

## Data Source

The follower count data in this game is for educational purposes only and may not reflect the current follower counts.

## Credits

This project was created as part of the "100 Days of Code - Python Pro Bootcamp".

## License

This project is open source and available for personal and educational use.

---

Enjoy the game and see how many celebrities you can correctly rank!
