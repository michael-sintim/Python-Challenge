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

folder_path = r"C:\Users\user\Desktop\beginner\json"
file_path = os.path.join(folder_path,f"{name}_contact.json")

with open(rf"C:\Users\user\Desktop\beginner\json\{name}_contact.json", "w") as file:
    file.write(f"Name: {json_converter}\n")
    file.write(f"Number: {json_converter}\n")
        

