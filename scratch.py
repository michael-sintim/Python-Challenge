 #Personal Expense Tracker 
import json 
catergory = []
total_amount = []
description = []


# def save_json(category,total_amount, description):
#      data = {
#           "category":category,
#           "total_amount":total_amount,
#           "description":description,
#      }
#      with open('tracker.json','w') as file :
#           json.dumps(data,file,indent=4)
     
     


while True:
    try:
        print("1. Add new expense")
        print("2. View all expenses")
        print("3. Total expenses")
        print("4. Show expenses by Category")
        print("5. Exit Program")
        choice = input("Select an option: ")
    

        if choice == '1':
            input_amount = float(input("Input Amount: "))
            input_Category = input("Input Category: ")
            input_description = input("Input Description: ")
            catergory.append(input_Category)
            total_amount.append(input_amount)
            description.append(input_description )
            print("Thank you! you input is saved successfully\n")

        elif choice == '2':
            print(f"Your total expenses: {total_amount}")

        elif choice == '3':
                print(f"Total amount: {sum(total_amount)}")


        elif choice == '4':
             if not catergory:
                  print("=== No expenses Recorded yet ===\n")

             else:
                  for x,y,z in zip(catergory,total_amount,description):
                       zoo = print(f"Total amount: {y} Category: {x} Description: {z}")     
                             

        elif choice == "5":
             print("You have ended the program successfully\n")
             quit()

        with open('tracker_file.txt','w') as file:
            file.write(print(f"{zoo}"))   
           


    except ValueError:
        raise ValueError("Invalid Input\n")


    
    
    