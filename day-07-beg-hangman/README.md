# Hangman Game

A classic word-guessing game where players try to figure out a hidden word letter by letter before the hangman is completely drawn.

## Description

This Hangman implementation is a command-line game where players must guess letters to reveal a randomly selected word. With each incorrect guess, a part of the hangman is drawn. Players have 6 lives (incorrect guesses) before the game ends.

The game features:
- A library of 200+ words to guess
- ASCII art for the hangman at different stages
- Input validation to ensure only valid letters are accepted
- Tracking of previously guessed letters

## Game Components

The project consists of three Python files:
1. `main.py` - The main game logic
2. `hangman_words.py` - Contains the word list for the game
3. `hangman_art.py` - Contains ASCII art for the hangman and game logo

## How to Play

1. Ensure you have Python 3 installed on your system.
2. Download all three files (`main.py`, `hangman_words.py`, and `hangman_art.py`) into the same directory.
3. Run the game from your terminal/command prompt:
   ```
   python main.py
   ```
4. The game will:
   - Display the Hangman logo
   - Show blank spaces for each letter in the hidden word
   - Prompt you to guess a letter
5. For each guess:
   - If correct, the letter will be revealed in the word
   - If incorrect, you lose a life and part of the hangman is drawn
6. The game ends when either:
   - You correctly guess all the letters (win)
   - You run out of lives (lose)

## Example Gameplay

```
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/    
______

****************************6 of 6 LIVES LEFT****************************
Guess a letter: a
['a']
_a___
  +---+
  |   |
      |
      |
      |
      |
=========

****************************6 of 6 LIVES LEFT****************************
Guess a letter: b
You guessed b. That's not in the word.
_a___
  +---+
  |   |
  O   |
      |
      |
      |
=========

...
```

## Features and Logic

- **Word Selection**: The game randomly selects a word from a predefined list.
- **Input Validation**:
  - Checks that input is an actual letter
  - Prevents duplicate guesses
- **Life System**: Players have 6 lives (incorrect guesses) before losing
- **Visual Feedback**:
  - ASCII art shows the hangman's progress
  - Current state of the word is displayed after each guess
  - Clear win/lose messages

## Code Structure

- `main.py`:
  - Contains the game loop and core logic
  - Handles player input and game state
  - Displays game progress
- `hangman_words.py`:
  - Contains a list of 200+ words to be used in the game
- `hangman_art.py`:
  - Contains ASCII art for the hangman at different stages
  - Contains the game logo

## Customization

You can customize the game by:
- Adding more words to the `word_list` in `hangman_words.py`
- Modifying the ASCII art in `hangman_art.py`
- Adjusting the number of lives by changing the `lives` variable in `main.py`

## Credits

This project is part of the "100 Days of Code - Python Pro Bootcamp" curriculum.

## License

This project is open source and available under the [MIT License](https://opensource.org/licenses/MIT).
