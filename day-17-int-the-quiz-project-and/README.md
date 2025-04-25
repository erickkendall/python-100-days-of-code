# True/False Quiz Game

A Python-based quiz game that tests your knowledge with true/false questions fetched from the Open Trivia Database.

## Description

This True/False Quiz Game is an object-oriented Python application that presents users with a series of true/false questions on various topics. The game tracks your score as you play and displays your final result when you've answered all questions.

The game features:
- Real-time questions fetched from the Open Trivia Database API (opentdb.com)
- Object-oriented design with separate classes for questions and quiz logic
- Score tracking throughout the game
- Clean command-line interface
- Session token management to prevent duplicate questions

## Game Components

The project consists of three Python files:
1. `main.py` - Entry point, initialization of the quiz, and API integration
2. `question_model.py` - Contains the Question class
3. `quiz_brain.py` - Contains the QuizBrain class that manages quiz logic
4. `trivia_api.py` - Handles communication with the Open Trivia Database API

## How to Play

1. Ensure you have Python 3 installed on your system.
2. Make sure you have the `requests` library installed. If not, install it with:
   ```
   pip install requests
   ```
3. Download all three files (`main.py`, `question_model.py`, `quiz_brain.py`, and `trivia_api.py`) into the same directory.
4. Run the game from your terminal/command prompt:
   ```
   python main.py
   ```
5. The game will:
   - Connect to the Open Trivia Database API
   - Fetch a fresh set of true/false questions
   - Present each question one at a time
   - Prompt you to answer with "True" or "False"
6. For each guess:
   - The game will tell you if you're right or wrong
   - Your current score will be displayed
7. When all questions have been answered, your final score will be shown.

## Example Gameplay

```
Q.1: All strawberries are red. (True/False): False
You got it right!
The correct answer was: False
Your current score is: 1/1

Q.2: Gumbo is a stew that originated in Louisiana. (True/False): True
You got it right!
The correct answer was: True
Your current score is: 2/2

Q.3: Scotland voted to become an independent country during the referendum from September 2014. (True/False): False
You got it right!
The correct answer was: False
Your current score is: 3/3

...

Your final score is: 8/10
```

## Features and Logic

- **Object-Oriented Design**: The game uses OOP principles with separate classes for questions and quiz logic
- **Live API Integration**: Questions are fetched in real-time from the Open Trivia Database
- **Session Token Management**: Uses API tokens to prevent duplicate questions
- **Score Tracking**: The game keeps track of your score throughout
- **Clean User Interface**: Simple command-line interface with clear feedback

## Code Structure

- `main.py`:
  - Fetches fresh questions from the Open Trivia Database API
  - Creates the question bank from the question data
  - Initializes the quiz and runs the main game loop
- `question_model.py`:
  - Defines the Question class that stores question text and answer
- `quiz_brain.py`:
  - Contains the QuizBrain class with methods to:
    - Present questions
    - Check answers
    - Keep track of score
    - Determine when the quiz is complete
- `trivia_api.py`:
  - Handles communication with the Open Trivia Database API
  - Manages session tokens to prevent duplicate questions
  - Processes API responses and error handling

## Customization

You can customize the game by modifying the API call in `main.py`:

```python
# Get questions with specific parameters
question_data = get_trivia_questions(
    amount=10,             # Number of questions
    category=9,            # Category ID (9 = General Knowledge)
    difficulty="medium",   # Difficulty (easy, medium, hard)
    question_type="boolean" # Question type (boolean for True/False)
)
```

Available categories include:
- 9: General Knowledge
- 17: Science & Nature
- 18: Computers
- 19: Mathematics
- 22: Geography
- 23: History
- And many more...

## API Information

This game uses the Open Trivia Database API (https://opentdb.com/):
- The API is free to use with no authentication required
- A session token is used to prevent duplicate questions
- The API has rate limiting (no more than one request every 5 seconds)
- Questions are available in multiple categories and difficulty levels

For more information about the API, visit the Open Trivia Database website.

## Dependencies

- Python 3.6 or higher
- Requests library (`pip install requests`)

## Credits

This project is built using the object-oriented programming concepts from the "100 Days of Code - Python Pro Bootcamp."

Questions are sourced from the Open Trivia Database (https://opentdb.com), a free to use, user-contributed trivia question database.

## License

This project is open source and available under the [MIT License](https://opensource.org/licenses/MIT).
