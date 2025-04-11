name = input("Please enter your full name: ")
first_initial = name[0]
space_index = name.index(" ")
last_initial = name[space_index + 1]
initials = first_initial + last_initial
print(initials.upper())