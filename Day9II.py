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

contacts = []

contacts.append(x)

folder_path = r"C:\Users\user\Desktop\beginner\json"
file_path = os.path.join(folder_path,f"{name}_contact.json")

with open(file_path, "w") as file:
    json.dump(x,file,indent=4)
    

        

