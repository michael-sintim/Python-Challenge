#Day 10
## Build a program that converts between JSON and CSV formats with  serialization
#with type hints
import os 
import json
import csv
import pickle

name :str = input("Input name: ")
age = input("Input age: ")
email:str = input("Input email: ")

contact :dict[str,str|int]= {
    "Name":name,
    "Age" : age,
    "Email": email,
}

folder_path :str = r"C:\Users\user\Desktop\beginner\json"
file_path :str = os.path.join(folder_path,f"{name}_data.json")


with open(file_path,'w') as file:
    json.dump(contact,file,indent=4)

with open(file_path,'r') as file:
    data = json.load(file)

folder_path_csv :str = r"C:\Users\user\Desktop\beginner\csv_files"
file_path_csv :str= os.path.join(folder_path_csv,f"{name}.csv")

with open(file_path_csv,'w', newline="") as csvfile:
    fieldnames = data.keys()
    writer = csv.DictWriter(csvfile,fieldnames=fieldnames)
    writer.writeheader()
    writer.writerow(data)



while True:
    print("1. Load JSON and convert to CSV ")
    print("2. Load CSV and convert to JSON")
    print("3. Serialize current data ")
    print("4. Deserialize saved data ")
    print("5. Exit ")
    choice = input("Input your choice: ")

    if choice == "1":
        with open(file_path,'r') as file:
            data = json.load(file)

        with open(file_path_csv,'w', newline="") as csvfile:
        
            fieldnames = data.keys()
            writer = csv.DictWriter(csvfile,fieldnames=fieldnames)
            writer.writeheader()
            writer.writerow(data)

    elif choice == "2":
        with open (file_path_csv,"r") as csvfile:
            csv_file = list(csv.DictReader(csvfile))
            
        with open(file_path,'w') as jsonfile:
            json.dump(csv_file,jsonfile,indent=4)

    elif choice == "3":
        with open(f"{name}.pkl",'wb') as f:
            pickle.dump(data,f)
        
    
    elif choice == "4":
        with open(f"{name}.pkl",'rb') as f:
            loaded_data = pickle.load(f)

        print(f"Deserialized data: {loaded_data}")
        
    elif choice == "5":
        quit()
        