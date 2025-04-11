"""
    This is a space devoted to Lists, Slicing and how these are used and manipulated in Python
    Rememember! Lists are like arrays in C++
"""

# example list
ex_list = [1, 2, 3, 4, 5]
print(ex_list[0])
print(ex_list[-1])

print("The syntax of lists is the following: list[start:stop:step]")
# some examples of slicing
print("Print only the even numbers from the list: ")
print(ex_list[1:4:2])
# or also
print(ex_list[1::2])

# Let's do some list operations to get a better understanding
fruits = ["apple", "banana"]
fruits.append("orange") # adds the orange element at the end of the list
fruits.insert(1, "kiwi") # adds the element kiwi at position 1 and it moves the rest of the elements to the next and previous positions
print(fruits)

fruits.remove("banana")
fruits.pop() # automatically removes the element at the end of the list
fruits.pop(0) # removes an element at an exact position

# let's see some useful built-in functions often used with lists
fruits_length = len(fruits) # the number of elements in the list
sum_example = sum(ex_list) # only for numeric values
# getting the largest and smallest value 
example_max = max(ex_list)
# sorting, the function understands on its own
sorted(fruits) # alphabetical order

# Create a list of 5 favorite foods
count = 0
foods = []
while count < 5:
    foods.append(input("Enter a food: "))
    count += 1
    
print("Your favourite foods are: ")
for i in foods:
    print(i)

people = ["Arkouda", "Pepe", "Nouno", "Elena", "Androulla", "Antonis"]
print(people[:3])

print(people[-1:])

# matrices
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

for i in matrix:
    for j in i:
        print(j)

# compact list building
squares = [x**2 for x in range(1, 11)]
print(squares)

