class Student:
    # constructor
    def __init__(self, name, age, department):
        self.name = name
        self.age = age
        self.department = department
    
    # display student data
    def display(self):
        print(f"Student's name: {self.name}")
        print(f"Student's age: {self.age}")
        print(f"Student's Department: {self.department}")

# get the number of students in a class
number_of_students = int(input("How many students are in your class: "))
students = []

# prompt the user to enter student data
for i in range(number_of_students):
    # student name input, ensure there are only caracters and a space
    name = input(f"Enter the name of the student {i + 1}: ")
    while True:
        if " " not in name:
            print("Full name must contain at least a space between the name and the last name!")
            name = input(f"Enter the name of the student {i + 1}: ")
        else:
            break

    # take and check age input
    while True:
        try:
             age = int(input(f"Enter the age of student {i + 1}: "))
        except ValueError:
            print("The age must be a valid number!")
        else:
            break

    # take a department input
    department = input(f"Enter the department in which the student {i+1} belongs to: ")

    student = Student(name, age, department)
    students.append(student)

# create a dictionary
from collections import defaultdict

department_counts = defaultdict(int)
oldest_student = None
youngest_students = []

for student in students:
    department_counts[student.department] += 1
    
    if oldest_student is None or student.age > oldest_student.age:
        oldest_student = student

# Sort students by age to get three youngest
sorted_by_age = sorted(students, key=lambda s: s.age)
youngest_students = sorted_by_age[:3]

print(" ")
print("---- STUDENT INFORMATION ----\n")

for student in students:
    student.display()
    print("-"*20)

print("\n---- DEPARTMENT COUNTS ----")
for dept, count in department_counts.items():
    print(f"{dept}: {count} student(s)")

print("\n---- OLDEST STUDENT ----")
oldest_student.display()

print("\n---- THREE YOUNGEST STUDENTS ----")
for s in youngest_students:
    s.display()
    print("-" * 20)
