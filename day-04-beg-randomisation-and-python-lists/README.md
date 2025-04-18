# Rock Paper Scissors Game

A command-line implementation of the classic Rock Paper Scissors game where you play against the computer.

## Description

This Rock Paper Scissors game is a Python application created as part of the "100 Days of Code - Python Pro Bootcamp". The program demonstrates several Python programming concepts including:

- Randomization using the `random` module
- Conditional logic with if/elif/else statements
- Function definition and usage
- List manipulation
- ASCII art for visual elements
- String formatting and joining
- User input validation

Players choose between rock, paper, or scissors, and compete against a computer that randomly selects its move. The game displays ASCII art representations of each choice and determines the winner based on traditional Rock Paper Scissors rules.

## How to Play

1. Ensure Python is installed on your system.
2. Download the `main.py` file.
3. Run the program from your terminal/command prompt:
   ```
   python main.py
   ```
4. Enter your choice when prompted: "rock", "paper", or "scissors"
5. The computer will randomly select its move
6. The program will display both choices with ASCII art and announce the winner

## Game Rules

- Rock beats Scissors (rock smashes scissors)
- Paper beats Rock (paper covers rock)
- Scissors beats Paper (scissors cuts paper)
- Identical choices result in a tie

## Example Gameplay

```
Choose one: rock, paper, scissors: rock

    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)

User picks rock.

    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)

COMPUTER picks paper.
Paper covers rock. COMPUTER wins.
```

## Code Structure

The program includes:

- ASCII art for rock, paper, and scissors
- A function to display the appropriate ASCII art based on choice
- Input validation to ensure the user enters a valid choice
- Random selection for the computer's move
- Logic to determine and announce the winner based on the game rules

## Credits

This project is part of the "100 Days of Code - Python Pro Bootcamp" curriculum.

## License

This project is open source and available under the [MIT License](https://opensource.org/licenses/MIT).
