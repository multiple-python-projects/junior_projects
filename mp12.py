def celsius_to_fahrenheit(c):
    try:
        c = int(c)
        return (c * (9 / 5) + 32)
    except ValueError:
        print("Celsius must be a number!")

celsius = input("Please enter the temperature in celsius: ")
print(celsius_to_fahrenheit(celsius))