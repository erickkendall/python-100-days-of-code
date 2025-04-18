# Tip Calculator

A Python program that calculates how much each person should pay when splitting a bill with tip included.

## Description

This Tip Calculator is a simple Python application created as part of the "100 Days of Code - Python Pro Bootcamp". The program demonstrates several important Python concepts including:

- Working with various data types (strings, integers, floats)
- Type conversion
- Mathematical operations
- String formatting with f-strings
- User input handling
- Rounding numbers

The calculator takes the total bill amount, desired tip percentage, and number of people sharing the bill as inputs, then calculates and outputs the amount each person should pay.

## How to Use

1. Ensure Python is installed on your system.
2. Download the `main.py` file.
3. Run the program from your terminal/command prompt:
   ```
   python main.py
   ```
4. Follow the prompts to enter:
   - The total bill amount
   - The tip percentage (10%, 12%, or 15%)
   - The number of people splitting the bill
5. The program will calculate and display how much each person should pay.

## Example

```
Welcome to the tip calculator!
What was the total bill? $150.00
What percentage tip would you like to give? 10 12 15 12
How many people to split the bill? 5
Each person should pay: $33.6
```

## Code

```python
print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10 12 15 "))
people = int(input("How many people to split the bill? "))

total = bill + (bill*tip/100)
cost_per_person = total/int(people)
print(f"Each person should pay: ${round(cost_per_person,2)}")
```

## Skills Demonstrated

- Variables and data types (strings, integers, floats)
- Type conversion using `float()` and `int()`
- Mathematical operations (+, *, /)
- String formatting using f-strings
- User input with the `input()` function
- Rounding with the `round()` function

## Credits

This project is part of the "100 Days of Code - Python Pro Bootcamp" curriculum.

## License

This project is open source and available under the [MIT License](https://opensource.org/licenses/MIT).
