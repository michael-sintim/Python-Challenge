from Day7 import password_validator

while True: 
    
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
    
    if password_validator() == "Password accepted":

        history = []

        print("\n===SECURE CALCULATOR===")
        print("1. Perform calculation")
        print("2. View history")
        print("3. Clear history")
        print("4. Exit\n")
    
    choice = input("Input choice: ")


    if choice == '1':
        calculate()


    elif choice == '2':
        pass
    
    elif choice == '3':
        pass

    elif choice == '4':
        print("Your program is over")
        quit()
    
