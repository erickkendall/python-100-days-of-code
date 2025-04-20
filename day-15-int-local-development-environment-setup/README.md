# Coffee Machine

A Python command-line application that simulates a coffee vending machine with resource management, payment processing, and drink preparation functionality.

## Description

This Coffee Machine application simulates a real-world coffee vending machine that can prepare three popular coffee drinks. The program tracks available resources (water, milk, coffee), handles coin-based payments, and manages drink preparation when sufficient resources and correct payment are provided.

## Game Components

The project consists of a single Python file:
1. `coffee_machine.py` - Contains all game logic, resources, and menu definitions

## How to Use

1. Ensure you have Python 3 installed on your system.
2. Install the required dependency:
   ```
   pip install prettytable
   ```
3. Run the program from your terminal/command prompt:
   ```
   python coffee_machine.py
   ```
4. The program will prompt you to select a drink:
   ```
   What would you like? (espresso/latte/cappuccino):
   ```

## Available Commands

- **espresso/latte/cappuccino**: Order a drink
- **report**: Display current resource levels and profit
- **off**: Turn off the coffee machine (for maintainers only)

## Example Usage

```
What would you like? (espresso/latte/cappuccino): latte
A latte costs $2.50
How many quarters?: 10
How many dimes?: 0
How many nickels?: 0
How many pennies?: 0
Here is $0.00 in change.
Here is your latte. Enjoy!

What would you like? (espresso/latte/cappuccino): report

COFFEE MACHINE REPORT:
Water: 100ml
Milk: 50ml
Coffee: 76g
Money: $2.50
```

## Features and Logic

- **Drink Menu**: Offers espresso, latte, and cappuccino with different resource requirements and prices
- **Resource Management**: Tracks water, milk, and coffee inventory
- **Payment Processing**: 
  - Accepts four types of coins (quarters, dimes, nickels, pennies)
  - Calculates total payment amount
  - Provides change when necessary
  - Refunds insufficient payments
- **Resource Verification**:
  - Checks if sufficient resources exist before processing payment
  - Prevents resource depletion by declining orders when resources are low
- **Reporting**: Generates detailed reports of current resources and profit
- **Maintainer Access**: Secret "off" command to shut down the machine

## Code Structure

- **Global Constants**:
  - `MENU`: Dictionary containing drink recipes and prices
  - `resources`: Dictionary tracking available resources
- **Functions**:
  - `print_report()`: Displays formatted resource and profit information
  - `process_coins()`: Handles user payment input and verification
  - `verify_resources()`: Checks if resources are sufficient for selected drink
  - `coffee_machine()`: Main function that runs the coffee machine

## Coffee Drink Specifications

| Drink      | Water (ml) | Milk (ml) | Coffee (g) | Price ($) |
|------------|------------|-----------|------------|-----------|
| Espresso   | 50         | 0         | 18         | 1.50      |
| Latte      | 200        | 150       | 24         | 2.50      |
| Cappuccino | 250        | 100       | 24         | 3.00      |

## Customization

You can customize the coffee machine by:
- Adding more drinks to the `MENU` dictionary
- Adjusting resource quantities in the `resources` dictionary
- Changing drink prices or ingredient requirements
- Adding new resources (e.g., chocolate, sugar)

## Credits

This project is part of the "100 Days of Code - Python Pro Bootcamp" curriculum (Day 15).

## License

This project is open source and available under the [MIT License](https://opensource.org/licenses/MIT).
