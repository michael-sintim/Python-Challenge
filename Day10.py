#Day 10
## Build a program that converts between JSON and CSV formats with  serialization

import os 
import json
import csv
import pickle

name = input("Input name: ")
age = input("Input age: ")
email = input("Input email: ")

contact = {
    "Name":name,
    "Age" : age,
    "Email": email,
}

folder_path = r"C:\Users\user\Desktop\beginner\json"
file_path = os.path.join(folder_path,f"{name}_data.json")

with open(file_path,'w') as file:
    json.dump(contact,file,indent=4)

while True:
    print("1. Load JSON and convert to CSV ")
    print("2. Load CSV and convert to JSON")
    print("3. Serialize current data ")
    print("4. Deserialize saved data ")
    print("5. Exit ")
    choice = input("Input your choice: ")

    if choice == "1":
        with open(file_path,"r") as file:
            loaded_file = json.load(file)
            csv.DictWriter(file)

    elif choice == "2":
        csv.DictReader(file)
        json.dump(file)

    elif choice == "3":
        pickle.dump(file)

    elif choice == "4":
        pickle.loads(file)

    elif choice == "5":
        quit()
        