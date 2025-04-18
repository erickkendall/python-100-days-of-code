# Secret Auction Program

A Python program that simulates a secret auction where participants can place bids without seeing others' offers.

## Description

This Secret Auction program is a command-line tool created as part of the "100 Days of Code - Python Pro Bootcamp". The program demonstrates several Python programming concepts including:

- Working with dictionaries to store data
- Conditional statements and loops
- User input handling
- Finding maximum values from a collection

The auction allows multiple bidders to enter their names and bid amounts privately. Once all bids are submitted, the program determines and announces the highest bidder.

## Features

- Private bidding process (bidders don't see each other's bids)
- Support for multiple bidders
- Automatic determination of the highest bid
- User-friendly interface with ASCII art
- Input validation

## How to Use

1. Ensure Python is installed on your system.
2. Download both files (`main.py` and `art.py`) into the same directory.
3. Run the program from your terminal/command prompt:
   ```
   python main.py
   ```
4. For each bidder:
   - Enter the bidder's name
   - Enter their bid amount
   - Indicate whether there are more bidders
5. When all bids are submitted, the program will determine and announce the winner.

## Example Usage

```
                        ___________
                        \         /
                         )_______(
                         |"""""""|_.-._,.---------.,_.-._
                         |       | | |               | | ''-.
                         |       |_| |_             _| |_..-'
                         |_______| '-' `'---------'` '-'
                         )"""""""(
                        /_________\
                      .-------------.
                     /_______________\

What is the person's name? Alice
How much is your bid? 500
Any more bids? yes
What is the person's name? Bob
How much is your bid? 750
Any more bids? yes
What is the person's name? Charlie
How much is your bid? 600
Any more bids? no
The winner is: Bob with a bid of $750
```

## How It Works

The program utilizes a dictionary to store each bidder's name and their bid amount. After all bids are collected, it iterates through the dictionary to find the highest bid and the corresponding bidder.

The process works as follows:
1. A dictionary (`bidder_data`) is created to store bidder names and amounts
2. The program enters a loop to collect bids:
   - Asks for a bidder's name
   - Asks for their bid amount
   - Stores the name and amount in the dictionary
   - Asks if there are more bidders
3. When no more bidders remain, the program:
   - Initializes variables to track the highest bid and bidder
   - Iterates through all the bids to find the highest one
   - Announces the winner with their bid amount

## Code Structure

The project consists of two Python files:

1. `main.py` - Contains the main program logic:
   - Collects bidder information
   - Tracks and compares bids
   - Determines and announces the winner

2. `art.py` - Contains the ASCII art logo displayed at program start

## Possible Enhancements

- Clear the screen between bidders for more privacy
- Add support for decimal bid amounts
- Handle tied bids
- Add validation for bid amounts (only accept numbers)
- Implement minimum bid increments

## Credits

This project is part of the "100 Days of Code - Python Pro Bootcamp" curriculum.

## License

This project is open source and available under the [MIT License](https://opensource.org/licenses/MIT).
