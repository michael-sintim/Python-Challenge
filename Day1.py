
from datetime import datetime

RED = '\033[91m'
GREEN = '\033[92m'
YELLOW = '\033[93m'
BLUE = '\033[94m'
RESET = '\033[0m'

while True:
    name = input("What is your name: ")
    if name.replace(" ", "").isalpha():
        break
    else:
        print(f"{RED}Invalid input, alphabets only{RESET}")

while True:
    try:
        height = float(input("What is your height in cm: "))
        weight = float(input("What is your weight in Kg: "))
        age = int(input("What is your age: "))
        favourite_number = float(input("What is your favourite number: "))
        if height <= 0 or weight <= 0 or age <= 0:
            print(f"{RED}Positive numbers only{RESET}")
        else:
            break
    except ValueError:
        print(f"{RED}Input must be in numbers{RESET}")

current_year = datetime.now().year  
year_of_birth = current_year - age
age_in_ten_years = age + 10 
favourite_number_squared = favourite_number**2
height_m = height / 100
height_feet = height / 30.48
BMI = weight / height_m ** 2
days_alive =  age * 365.25  
hours_alive = days_alive * 24

life_expectancy = 80 
percentage_progress = (age / life_expectancy) * 100
progress_block = round(percentage_progress / 5)
remaining_blocks = 20 - progress_block

progress_bar = "█" * progress_block
remaining_bar = "░" * remaining_blocks

def color_bmi(BMI):

    
    if BMI < 0:
        return f"{RED}INVALID BMI{RESET}"
    elif BMI < 18.5:
        return f"{YELLOW}Underweight{RESET}"
    
    elif BMI >=18.5 and BMI <= 24.9:
        return f"{GREEN}Healthy{RESET}"
    elif BMI >=25 and BMI <= 29.9:
        return f"{BLUE}Overweight{RESET}"
    else:
        return f"{RED}Obese{RESET}"


print(f"{BLUE}Your Name: {name}{RESET}")
print(f"Your Age: {age}")
print(f"Your Favourite number: {favourite_number}")
print(f"Your Year of birth: {year_of_birth}")
print(f"Your Age in ten years: {age_in_ten_years}")
print(f"Your Favourite number squared: {favourite_number_squared}")
print(f"Your Height in cm: {height}")
print(f"Your Height in feet: {height_feet}")
print(f"Your BMI :{BMI} - {color_bmi(BMI)}")
print(f"Your Hours alive: {hours_alive}")
print(f"Your days alive are: {days_alive}")
print(f"Life Progress: [{progress_bar}{remaining_bar}] {percentage_progress:.1f}%")

with open(f"{name}_stats.txt", "w") as file:
    file.write(f"Your Name: {name}\n")
    file.write(f"Your Age: {age}\n")
    file.write(f"Your Favourite number: {favourite_number}\n")
    file.write(f"Your Year of birth: {year_of_birth}\n")
    file.write(f"Your Age in ten years: {age_in_ten_years}\n")
    file.write(f"Your Favourite number squared: {favourite_number_squared}\n")
    file.write(f"Your Height in cm: {height}\n")
    file.write(f"Your Height in feet: {height_feet}\n")
    file.write(f"Your BMI: {BMI} \n")
    file.write(f"Your Hours alive: {hours_alive}\n")
    file.write(f"Your days alive are: {days_alive}\n")

print(f"{GREEN}Your stats have been saved successfully!{RESET}")