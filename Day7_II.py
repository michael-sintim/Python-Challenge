"""
Secure Calculator Module.

This module provides a secure calculator that requires password authentication
before performing calculations. It maintains a history of all calculations.
"""

from Day7 import password_validator


def perform_calculation() -> tuple:
    """
    Perform a calculation based on user input.
    
    Returns:
        tuple: A tuple containing (result, calculation_string) or (None, None) on error
    """
    try:
        x = float(input("Input first number: "))
        y = float(input("Input second number: "))
        operand = input("Input operand (+, -, *, /, **, %): ")

        if operand == '/' and y == 0:
            print("Cannot divide by zero")
            return None, None

        if operand == '%' and y == 0:
            print("Cannot modulo by zero")
            return None, None

        if operand == "+":
            calculation_result = x + y
        elif operand == "-":
            calculation_result = x - y
        elif operand == "*":
            calculation_result = x * y
        elif operand == "/":
            calculation_result = x / y
        elif operand == "**":
            calculation_result = x ** y
        elif operand == "%":
            calculation_result = x % y
        else:
            print(f"Error: invalid operand '{operand}'")
            return None, None

        calculation_string = f"{x} {operand} {y} = {calculation_result}"
        return calculation_result, calculation_string

    except ValueError:
        print("Invalid input: please enter valid numbers")
        return None, None
    except ZeroDivisionError:
        print("Invalid operation: division by zero")
        return None, None


if password_validator() == "Password accepted":
    print("\n✅ Authentication successful!\n")

    history = []

    while True:
        print("\n=== SECURE CALCULATOR ===")
        print("1. Perform calculation")
        print("2. View history")
        print("3. Clear history")
        print("4. Exit\n")

        choice = input("Input choice: ")

        if choice == '1':
            result, calc_string = perform_calculation()
            if result is not None:
                print(f"\n{calc_string}")
                history.append(calc_string)

        elif choice == '2':
            if not history:
                print("No history yet")
            else:
                print('\n' + "=" * 50)
                print("Calculation History")
                print("=" * 50)

                for index, calc in enumerate(history, 1):
                    print(f"{index}. {calc}")

                print("=" * 50 + '\n')

        elif choice == '3':
            history.clear()
            print("History cleared")

        elif choice == '4':
            print("Goodbye!")
            break

        else:
            print("Invalid choice")
