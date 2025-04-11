# a dictionary stores key-value pairs
person = {
    "name" : "Alice",
    "age" : 25,
    "city" : "New York"
}

print(person["name"])
# we use get to be sure the key exists
print(person.get("age"))

# adding or updating a value
person["job"] = "Data Scientist"
del person["city"]

# loop through dictionary
for i in person:
    print(i, "->", person[i])
    
print("\nThere is also another way: ")
for i, value in person.items():
    print(i, "=", value)

# returning all the keys
person.keys()
# return all the values
values = person.values()
print(values)
print(person.items()) # returns (key, value) pairs

students = {
    "name" : ["Nicolas", "Arkouda", "Pepe"],
    "age" : [21, 25, 9],
    "profession" : ["Data Scientist and Mathematician", "Graphic Design", "Student"]
}

print(students)