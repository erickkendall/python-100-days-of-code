# Day 15 - Local Development Environment Setup & the Coffee Machine
# 100 Days of Code - Python Pro Bootcamp

from prettytable import PrettyTable

MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def print_report(resources, profit=0):
    """Prints a formatted report of current resources and profit"""
    print("\nCOFFEE MACHINE REPORT:")
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Money: ${profit:.2f}")


def process_coins(menu, coffee_choice):
    """Process inserted coins and check if payment is sufficient"""
    is_sufficient = False
    amount_collected = 0.0
    quarters = 0
    dimes = 0
    nickels = 0
    pennies = 0

    print(f'A {coffee_choice} costs ${menu[coffee_choice]["cost"]:.2f}')
    while not is_sufficient:
        quarters = int(input("How many quarters?: "))
        dimes = int(input("How many dimes?: "))
        nickels = int(input("How many nickels?: "))
        pennies = int(input("How many pennies?: "))

        amount_collected = (quarters * 0.25) + (dimes * 0.10) + (nickels * 0.05) + (pennies * 0.01)

        if amount_collected < menu[coffee_choice]["cost"]:
            print(f"Sorry that's not enough money. ${amount_collected:.2f} refunded.")
            break
        elif amount_collected > menu[coffee_choice]["cost"]:
            change = amount_collected - menu[coffee_choice]["cost"]
            print(f"Here is ${change:.2f} in change.")
            is_sufficient = True
        else:
            is_sufficient = True
     
    return is_sufficient


def verify_resources(resources, menu, coffee_choice):
    """Check if there are sufficient resources and return updated resources if possible"""
    ingredients_needed = menu[coffee_choice]['ingredients']
    
    # Check if all required ingredients are available
    sufficient_resources = all(resources.get(ingredient, 0) >= amount
                              for ingredient, amount in ingredients_needed.items())
    
    # If resources are insufficient
    if not sufficient_resources:
        for ingredient, amount in ingredients_needed.items():
            if resources.get(ingredient, 0) < amount:
                print(f"Sorry, there is not enough {ingredient}.")
        return False, resources  # Return original resources unmodified
    
    # If resources are sufficient, subtract the required amounts
    updated_resources = resources.copy()  # Create a copy to avoid modifying the original
    for ingredient, amount in ingredients_needed.items():
        updated_resources[ingredient] -= amount
    
    return True, updated_resources


def coffee_machine():
    """Main function to run the coffee machine program"""
    profit = 0
    is_on = True
    current_resources = resources.copy()
    
    while is_on:
        # 1. Prompt user for input
        choice = input("\nWhat would you like? (espresso/latte/cappuccino): ").lower()
        
        # 2. Turn off coffee machine if "off" is entered
        if choice == "off":
            print("Coffee machine shutting down.")
            is_on = False
        
        # 3. Print report when "report" is entered
        elif choice == "report":
            print_report(current_resources, profit)
        
        # Process drink orders
        elif choice in MENU:
            # 4. Check if resources are sufficient
            resources_sufficient, updated_resources = verify_resources(current_resources, MENU, choice)
            
            # 5 & 6. Process coins and check transaction if resources are sufficient
            if resources_sufficient:
                payment_successful = process_coins(MENU, choice)
                
                # 7. Make coffee if payment is successful
                if payment_successful:
                    # Add cost to profit
                    profit += MENU[choice]["cost"]
                    
                    # Update resources
                    current_resources = updated_resources
                    
                    print(f"Here is your {choice}. Enjoy!")
        
        else:
            print("Invalid selection. Please try again.")


# Run the coffee machine
if __name__ == "__main__":
    coffee_machine()
