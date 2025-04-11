"""
Create a Python script that:
-
Create an array (list) that holds the grading categories:
"Fail", "Poor", "Fair", "Good", "Excellent"

Ask the user to enter a grade (an integer between 1 and 100). Assume the user
provides a valid input.

Classify the grade based on the following scale:

0 - 49 → "Fail"
50 - 64 → "Poor"
65 - 74 → "Fair" 
75 - 89 → "Good"
90 - 100 → "Excellent"

Use the list to print the correct category. 
"""

grade_cat = ["Fail", "Poor", "Fair", "Good", "Excellent"]
grade = int(input("Please enter the grade of the student: "))
while grade not in range(0, 101):
    grade = int(input("Please enter the grade of the student again: "))

if grade in range(0, 50):
    print(grade_cat[0])
elif grade in range(50, 65):
    print(grade_cat[1])
elif grade in range(65, 75):
    print(grade_cat[2])
elif grade in range(75, 90):
    print(grade_cat[3])
else:
    print(grade_cat[4])