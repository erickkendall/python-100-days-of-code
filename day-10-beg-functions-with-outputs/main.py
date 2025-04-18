# Day 10 - Functions with Outputs
# 100 Days of Code - Python Pro Bootcamp
from art import logo

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b != 0:
        return a / b
    else:
        return "Error: division by 0."

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}
print(logo)
def calculator():
    current_value = float(input("What is the first number?: "))
    
    while True:
        for operator in operations:
            print(operator)
        
        chosen_operator = input("Pick an operation: ")
        next_value = float(input("What is the next number?: "))
        
        calculation_result = operations[chosen_operator](current_value, next_value)
        print(f"{current_value} {chosen_operator} {next_value} = {calculation_result}")
        
        should_continue = input(f"Type 'y' to continue calculating with {calculation_result}, or type 'n' to start a new calculation: ")
        if should_continue == 'n':
            print("\n" * 20)
            calculator()  # Recursive call to restart
        else:
            current_value = calculation_result

calculator()
