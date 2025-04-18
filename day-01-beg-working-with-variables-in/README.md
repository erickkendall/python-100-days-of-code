# Band Name Generator

A simple Python program that generates band name suggestions by combining the user's hometown and pet name.

## Description

This Band Name Generator is a beginner-friendly Python application created as part of the "100 Days of Code - Python Pro Bootcamp". The program demonstrates fundamental Python concepts including:

- Printing to the console
- Taking user input
- Variable assignment
- String concatenation

When run, the program asks the user for their hometown and pet's name, then combines these inputs to suggest a unique band name.

## How to Use

1. Make sure you have Python installed on your computer.
2. Download the `band_name_generator.py` file.
3. Run the program from your terminal/command prompt:
   ```
   python band_name_generator.py
   ```
4. Follow the prompts to enter your hometown and pet's name.
5. Receive your generated band name!

## Example

```
Welcome to the Band Name Generator.
What's the name of the city your grew up in?
London
What's your pet's name?
Rex
Your band name could be London Rex
```

## Code

```python
print("Welcome to the Band Name Generator.")
city = input("What's the name of the city your grew up in?\n")
pet = input("What's your pet's name?\n")
print("Your band name could be " + city + " " + pet)
```

## Skills Demonstrated

- Using the `print()` function
- Using the `input()` function
- Storing user input in variables
- String manipulation/concatenation
- Basic program flow

## Credits

This project is part of the "100 Days of Code - Python Pro Bootcamp" curriculum.

## License

This project is open source and available under the [MIT License](https://opensource.org/licenses/MIT).
