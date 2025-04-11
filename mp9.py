# we define a student class which contains student information and methods
class Student:
    # constructor
    def __init__(self, full_name, age, student_id, department):
        self.full_name = full_name
        self.age = age
        self.student_id = student_id
        self.department = department

    # greeting function
    def greeting(self):
        print(f"Hello {self.full_name}. You are {self.age} and you are enrolled at the department {self.department} with student ID {self.student_id}.")

# take inputs from the user
full_name = input("Please enter your full name: ")
age = input("Please enter your age: ")
student_id = input("Please enter your student ID: ")
department = input("Please enter the department you are enrolled: ")

# validation of the full name
if " " not in full_name:
    print("Full name must contain at least a space between the name and the last name!")
    exit()

# check if age is only digits
if not age.isdigit():
    print("The age must be a number!")
    exit()
else:
    age = int(age)
    if age < 18 or age > 90:
        print("Age must be between 18 and 90 years old!")
        exit()

# student ID validation
if len(student_id) != 9 or student_id[0] != 'U' or student_id[4] != 'N' or not (student_id[1:4].isdigit() and student_id[5:].isdigit()):
    print("Invalid student ID format!")
    exit()

student = Student(full_name, age, student_id, department)
student.greeting()