
while True:
    try:
        a = int(input("Please enter a number: "))
        b = int(input("Please enter a second number: "))
        c = a / b
    except ValueError:
        print("Not a number!")
    except ZeroDivisionError:
        print("The second number is equal to zero!")
    else:
        print(c)
        break

