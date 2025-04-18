# Python Calculator

A simple command-line calculator application built with Python as part of the "100 Days of Code - Python Pro Bootcamp".

## Features

- Basic arithmetic operations:
  - Addition (+)
  - Subtraction (-)
  - Multiplication (*)
  - Division (/)
- Chain calculations with previous results
- Error handling for division by zero
- ASCII art calculator display

## Files

- `main.py` - The main calculator program
- `art.py` - Contains the ASCII art for the calculator logo

## How to Use

1. Run the program using Python:
   ```
   python main.py
   ```

2. Enter the first number when prompted
3. Choose an operation from the available options (+, -, *, /)
4. Enter the next number
5. View the result
6. Choose to continue with the result or start a new calculation

## Example Usage

```
What is the first number?: 10
+
-
*
/
Pick an operation: +
What is the next number?: 5
10.0 + 5.0 = 15.0
Type 'y' to continue calculating with 15.0, or type 'n' to start a new calculation: y
+
-
*
/
Pick an operation: *
What is the next number?: 2
15.0 * 2.0 = 30.0
Type 'y' to continue calculating with 30.0, or type 'n' to start a new calculation: n

[New calculation starts]
```

## Possible Improvements

- Add more complex operations (power, square root, etc.)
- Implement memory functions
- Add a history of calculations
- Replace recursive function call with a loop structure to prevent potential stack overflow
- Add input validation for operation selection

## Credits

This project is part of "100 Days of Code - Python Pro Bootcamp".
