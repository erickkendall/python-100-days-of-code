# Blackjack Game

A Python command-line implementation of the classic casino card game Blackjack (also known as 21).

## Description

This Blackjack game simulates the classic card game where players try to get card values as close to 21 as possible without going over. The program handles all game logic including dealing cards, player decisions, dealer AI, and determining the winner based on final hand values.

## Game Components

The project consists of a single Python file:
1. `blackjack.py` - Contains all game logic, card values, and functions

## How to Play

1. Ensure you have Python 3 installed on your system.
2. Run the program from your terminal/command prompt:
   ```
   python blackjack.py
   ```
3. You'll be dealt two cards to start
4. The dealer will show one card face up
5. Choose to "hit" (take another card) or "stand" (keep your current hand)
6. Get as close to 21 as possible without going over ("busting")
7. After you stand, the dealer plays according to fixed rules
8. The higher hand wins, as long as it doesn't exceed 21

## Game Rules

- The deck contains cards with values: Ace (11), 2-10 (face value), and face cards (10)
- Both player and dealer receive two cards initially
- Player can see both their own cards but only one of the dealer's cards
- Player goes first and can take as many cards as desired
- If player exceeds 21, they bust and lose immediately
- Dealer must hit until reaching at least 17 points
- If dealer busts, player wins
- Blackjack (21 with initial two cards) beats any other hand
- Equal scores result in a tie ("push")

**Note about Aces**: In this simplified implementation, Aces are always counted as 11 points. This differs from standard Blackjack rules where Aces can count as either 1 or 11 points (whichever benefits the player). This limitation means that certain strategic plays involving Aces are not possible in this version.

## Example Gameplay

```
Your cards: [10, 8], current score: 18
Dealer's first card: 4

Type 'y' to get another card, type 'n' to pass: n

Dealer's turn. Dealer's cards: [4, 10], score: 14
Dealer's cards: [4, 10, 9], current score: 23
Bust!

Final scores - You: 18, Dealer: 23
Dealer busted! You win!
```

## Features and Logic

- **Random Card Dealing**: Cards are randomly selected from a simulated deck
- **Automatic Scoring**: Hand values are calculated automatically
- **Dealer AI**: Dealer follows standard casino rules (must hit until 17+)
- **Special Cases**: Handles blackjacks, busts, and pushes correctly
- **User Interface**: Clear text prompts and game state information

## Code Structure

- **Global Constants**:
  - `CARDS`: List of possible card values
  - `BLACK_JACK`: The target score (21)
  - `DEALER_MINIMUM`: Minimum score for dealer to stand (17)
- **Functions**:
  - `deal_card()`: Returns a random card from the deck
  - `hit_me()`: Adds a card to a hand and evaluates the result
  - `play_blackjack()`: Main game function that handles the game flow

## Limitations

- **Fixed Ace Values**: The current implementation treats Aces as having a fixed value of 11, rather than allowing them to be counted as either 1 or 11 as in standard Blackjack rules.
- **No Hand Splitting**: The game doesn't support splitting pairs into two separate hands.
- **No Double Down**: Players cannot double their bet in favorable situations.
- **No Betting System**: The game tracks wins and losses but doesn't implement a betting system with chips.

## Customization

You can customize the game by:
- Modifying the `DEALER_MINIMUM` to change dealer behavior
- Adding card suits for a more realistic experience
- Implementing more advanced rules like splitting pairs or doubling down
- Adding a betting system for extended gameplay
- **Implementing dynamic Ace values**: Create a function to evaluate Aces as either 1 or 11 based on the current hand total, which would make the game follow standard Blackjack rules more accurately

## Credits

This project is part of the "100 Days of Code - Python Pro Bootcamp" curriculum (Day 11).

## License

This project is open source and available under the [MIT License](https://opensource.org/licenses/MIT).
