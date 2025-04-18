# Day 5 - Python Loops
# 100 Days of Code - Python Pro Bootcamp

# Your code here
import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")

nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input("How many symbols would you like?\n"))
nr_numbers = int(input("How many numbers would you like?\n"))

# APPROACH 1: Using a list to build the password (recommended)
# ----------------------------------------------------------------
# Advantage: Lists are mutable so they can be shuffled directly
# without conversion steps
password_list = []

for char in range(0, nr_letters):
    password_list.append(random.choice(letters))

for symbol in range(0, nr_symbols):
    password_list.append(random.choice(symbols))

for num in range(0, nr_numbers):
    password_list.append(random.choice(numbers))

# Shuffle the password list in place
random.shuffle(password_list)

# Convert list to string
password = "".join(password_list)

print(f"Your password is: {password}")


# APPROACH 2: Using a string to build the password (alternative)
# ----------------------------------------------------------------
# Advantage: Slightly simpler code, but requires conversion for shuffling
# since strings are immutable in Python

# Build the password as a string - characters will be grouped by type
password_string = ""

for char in range(0, nr_letters):
    password_string += random.choice(letters)

for symbol in range(0, nr_symbols):
    password_string += random.choice(symbols)

for num in range(0, nr_numbers):
    password_string += random.choice(numbers)

# To shuffle a string, convert to list first
password_chars = list(password_string)
random.shuffle(password_chars)
shuffled_password = ''.join(password_chars)

print(f"Alternative approach password: {shuffled_password}")

# NOTE: Choose one approach or the other for your final code
# Having both is just for demonstration purposes
