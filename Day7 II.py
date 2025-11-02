from Day7 import password_validator

def calculate()-> float:
        
        try:
            x = float(input("Input a number:"))
            y = float(input("Input a number:"))
            operand = input("Input a operand:")

            if  operand == '/' and y == 0:
                print("Can't divide by 0")
                return(None,None)
            
            elif  operand == '%' and y == 0:
                print("Can't divide by 0")
                return(None,None)
            
            elif operand == "+":
                result = x + y

            elif operand == "-":
                result = x -y

            elif operand == "*":

                result = x * y
            elif operand == "/":
                result = x / y
            elif operand == "**":
                result = x ** y
            elif operand == "%":
                result = x % y
            
            else:
                print(f'Error, invalid operand: {operand}')
                
                return (None,None)
            

            calc_string = f"{x} {operand} {y} = {result}"
            return (result,calc_string)
        

        except ValueError:
            print("Invalid input")
            return None
        except ZeroDivisionError:
            print("Invalid input")
            return None
    
    
    
    
if password_validator() == "Password accepted":
    print("\n✅ Authentication successful!\n")

        
   
    history = []

    while True: 
        print("\n===SECURE CALCULATOR===")
        print("1. Perform calculation")
        print("2. View history")
        print("3. Clear history")
        print("4. Exit\n")

        choice = input("Input choice: ")

        if choice == '1':
            result, calc_string  = calculate()
            if result is not None:
                print()
                print(f" {calc_string}")
                history.append(calc_string)


        elif choice == '2':
            if not history:
                print("No history yet")
            # print(f"History: ",history if history else "No history yet") 
            # 
            else:
                print('\n'+ "="*50)  
                print("Calculation History")
                print("="*50)

                for x, calc in enumerate(history,1):
                    print(f'{x}.{calc}')

                print("="*50 + '\n')
        elif choice == '3':
            history.clear()
            print("You have cleared all history")

        elif choice == '4':
            print("Your have exited the program")
            quit()
        else:
            print("Invalid Choice")
