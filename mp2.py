"""
Create a Python script that::
-
Ask the user (i) for their age and (ii) whether they have a VIP pass (yes or no). Again
assume that the user gives correct input.
-
A person can enter the event if:
-
They are 18 or older, OR
-
They have a VIP pass (regardless of age).
-
Print "Access granted!" if they meet the conditions, otherwise print "Access denied!"
.
"""

age = int(input("Please neter your age: "))
pass_vip = input("Please enter yes or no if you have a vip pass: ").lower()
while pass_vip != "yes" and pass_vip != "no":
    pass_vip = input("Please re-enter yes or no if you have a vip pass: ").lower

if age >= 18 and pass_vip == "yes":
    print("Access granted!")
else:
    print("Access denied!")