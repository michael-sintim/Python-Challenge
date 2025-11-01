#weekly assessment from day one 
def password_validator():
    while True:
        special_chars = "!@#$%^&*()_+-=[]{}|;:,.<>?"
        password  = input("Input Password: ")
        # confrim_password = input("Confirm Password: ")

        errors = []
        if len(password) < 8:
            errors.append("Must be at least 8 characters")


        if  not any(char in special_chars for char in password):
            errors.append("Must have special characters in them")


        if not any(char.isupper()for char in password):
            errors.append("Must have at least one uppercae letter ")



        if not any(char.islower()for char in password):
            errors.append("Must have at least one lowercae letter ")



        if not any(char.isdigit() for char in password):
            errors.append("Must have at least one digit ")




        #strength validator

        strength = 0
        if len(password) > 8 :
            strength += 20

        if   any(char in special_chars for char in password):
            strength += 20

        if  any(char.isupper()for char in password):
            strength += 20

        if  any(char.isdigit() for char in password):
            strength += 20

        if  any(char.islower()for char in password):
            strength += 20

        
        print(f"Password strength: {strength}/100")

        
        if errors:
            print("Validation failed ")
            for error in errors:
                print(f"error- {error}")
               
            
        else: 
            
            print("Password accepted")
            return "Password accepted" 
        


        

if __name__ == "__main__":
    password_validator()

            

