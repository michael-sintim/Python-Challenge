import statistics

student_name_book = {
    "Ike": {"Math": 85, "English": 85, "Science": 90, "Coding": 67},
    "Kofi": {"Math": 78, "English": 94, "Science": 76, "Coding": 86},
    "Ama": {"Math": 87, "English": 74, "Science": 90, "Coding": 70},
}

# Add a new student
student_name_book["John"] = {
    "Math": 87,
    "English": 87,
    "Science": 90,
    "Coding": 70,
}

# Dictionary to store averages
averages = {}

# Loop through each student and calculate their average
for name, grades in student_name_book.items():
    avg = statistics.mean(grades.values())
    averages[name] = avg
    print(f"{name}'s average: {avg:.2f}")

# Find the student with the highest average
top_student = max(averages, key=averages.get)
print(f"\n🏆 Top student: {top_student} with an average of {averages[top_student]:.2f}")
