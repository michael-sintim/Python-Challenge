from Day7 import password_validator


if password_validator() == "Password accepted":
    print("\n===SECURE CALCULATOR===")
    print("1. Perform calculation")
    print("2. View history")
    print("3. Clear history")
    print("4. Exit\n")

choice = input("Input choice: ")

def calculate(x: float ,y: float,operand: str)-> float:
    x = float(input("Input a number:"))
    y = float(input("Input a number:"))
    operand = input("Input a operand:")

    try:
        
        if x/0 or y/0:
            raise ZeroDivisionError
        
        elif operand == "+":
            return x + y

        elif operand == "-":

            return x -y
        elif operand == "*":

            return x * y
        elif operand == "/":
            return x / y
        elif operand == "**":
            return x ** y
        elif operand == "%":
            return x % y
        
    except:
        raise ValueError("Invalid operand")
    
# if __name__ == "__main__":
    calculate()
