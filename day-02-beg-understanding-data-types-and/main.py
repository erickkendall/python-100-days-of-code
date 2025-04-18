# Day 2 - Understanding Data Types and How to Manipulate Strings
# 100 Days of Code - Python Pro Bootcamp

# Your code here
print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10 12 15 "))
people = int(input("How many people to split the bill? "))

total = bill + (bill*tip/100)
cost_per_person=total/int(people)
print(f"Each person should pay: {round(cost_per_person,2)}")
