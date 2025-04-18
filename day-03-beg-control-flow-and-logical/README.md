# Treasure Island

A text-based adventure game where you make choices to find the hidden treasure.

## Description

Treasure Island is a simple command-line adventure game created as part of the "100 Days of Code - Python Pro Bootcamp". This interactive game demonstrates fundamental programming concepts including:

- Conditional statements (if/else)
- User input handling
- String methods
- ASCII art integration
- Basic game logic

Players are presented with a series of choices that lead to different outcomes. Only one path leads to the treasure - choose wisely!

## How to Play

1. Make sure you have Python installed on your computer.
2. Download the `main.py` file.
3. Run the program from your terminal/command prompt:
   ```
   python main.py
   ```
4. Follow the prompts and make your choices by typing your response.
5. Try to find the treasure without meeting an untimely end!

## Game Preview

The game starts with an impressive ASCII art of a treasure island and presents you with a series of decisions:

1. First, choose to go left or right
2. Then, decide whether to swim across or wait
3. Finally, select one of three doors: red, blue, or yellow

Only one specific combination of choices will lead you to the treasure!

## Example Gameplay

```
*******************************************************************************
          |                   |                  |                     |
_________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      *`"=.*                     |
_________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ``` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
_________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     *.*;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************

Welcome to Treasure Island.
Your mission is to find the treasure.
What direction do you want to go, left or right? left
Do you want to swim across the water or wait? wait
Which door: red, blue, or yellow? yellow
You won!
```

## Code Structure

The game uses nested conditional statements to create the decision tree:
- Going right at the first choice leads to game over
- Swimming instead of waiting leads to game over
- Choosing the wrong door (anything but yellow) leads to game over

The game features ASCII art for visual appeal and uses the `.lower()` method to handle user input case-insensitively.

## Credits

- ASCII art sourced from https://ascii.co.uk/art
- This project is part of the "100 Days of Code - Python Pro Bootcamp" curriculum.

## License

This project is open source and available under the [MIT License](https://opensource.org/licenses/MIT).
