# Number Guessing Game

A simple command-line number guessing game built with Python.

## Description

This is a fun and interactive number guessing game where the computer selects a random number between 1 and 100, and the player tries to guess it within a limited number of attempts.

## Features

- Random number generation between 1 and 100
- Two difficulty levels:
  - Easy: 10 attempts
  - Hard: 5 attempts
- Interactive feedback after each guess (too high/too low)
- Remaining attempts counter

## How to Play

1. Run the game using Python:
   ```
   python guessing_game.py
   ```

2. The computer will think of a number between 1 and 100
3. Choose your difficulty level: 'easy' or 'hard'
4. Make your guess
5. Receive feedback on whether your guess was too high or too low
6. Continue guessing until you find the correct number or run out of attempts

## Example Gameplay

```
Welcome to the Guessing Game!
I'm thinking of a number between 1 and 100.
Choose a difficulty. Type 'easy' or 'hard': easy
You have 10 attempts remaining to guess the number.
Make a guess: 50
Too low.
Guess again.
You have 9 attempts remaining to guess the number.
Make a guess: 75
Too high.
Guess again.
You have 8 attempts remaining to guess the number.
Make a guess: 62
You got it! The answer was 62
```

## Possible Improvements

- Add input validation to handle non-numeric inputs
- Implement a scoring system based on the number of attempts used
- Add an option to play again after the game ends
- Create a leaderboard to track the best scores
- Add a hint system for players who are struggling

## Requirements

- Python 3.x

## License

This project is open source and available under the MIT License.
