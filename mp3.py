# This is a program which shows how we use break and continue
print("BREAK means I am out of here")
print("CONTINUE means skips this one and move forward")

# the example below stops the loop when the value of the number reaches 5
for num in range(1, 10):
    if num == 5:
        print("Exiting the loop when number reaches the value of 5.")
        break
    print(num)

# the following code ignores values which can be divided exactly by 3
for num in range(1, 10):
    if num % 3 == 0:
        continue
    print(num)

# example of how we use the the break in while loop
i = 0
while True:
    print(i)
    if i == 3:
        break
    i += 1
print("We use break in while loops to prevent infinite loops.")

# how we use continue in while loops
j = 0
while j < 5:
    print(j)
    if j % 2 == 0:
        continue
    j += 1

# now let's  try to print numbers from one to 10 using a for loop and using a while loop
print("Let's print a number using a for loop")
for i in range(1, 11):
    print(i)
i = 1
while i < 11:
    print(i)
    i += 1

"""
    Write a program that prompts the user to enter numbers in a list until the count reaches 5
"""

# printing only odd numbers from 1 to 20
for i in range(1, 21):
    if i % 2 == 0:
        continue
    print(i)

# ask the user for a password
password = "AgOurka"
while True:
    user_pass = input("Please enter the password: ")
    if user_pass == password:
        print("Access accepted!")
        break

for i in range(1, 40):
    if i % 4 == 0 and i % 5 == 0:
        break
    print(i)

# print the sequence {an} = n + 2 for n belongs to [1, 20]
for i in range(1, 21, 2):
    print(i)