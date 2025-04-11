def check_if_valid(name, age, height):
    if not age.isdigit() or not height.isdigit():
        print("Invalid input! Age and height must be numbers!")
        exit()
    else:
        print(f"You are {name}, an {age} year old guy of {height} cm.")

name = input("Please enter your name: ")
age = input("Please enter your age: ")
height = input("Please enter your height: ")

check_if_valid(name, age, height)
