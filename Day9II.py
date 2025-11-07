#Create a simple address book that stores contacts in JSON format
import os 
import json


name = input("Input your name: ")
number = input("Input your number: ")



x = {

    "name":name,
    "number": number

}

json_converter = json.dumps(x)

with open(rf"C:\Users\user\Desktop\beginner\json\{name}_contact.json", "w") as file:
    file.write(f"Name: {json_converter[name]}\n")
    file.write(f"Number: {json_converter[number]}\n")
        

