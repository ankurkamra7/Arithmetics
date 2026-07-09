# program to swap two variables.

# Input two variables
a = input("Enter the value of the first variable (a): ")
b = input("Enter the value of the second variable (b): ")
# Display the original values
print(f"Original values: a = {a}, b = {b}")
# Swap the values using a temporary variable
temp = a
a = b
# b = temp  # BUG: Missing line - swap is incomplete, b never gets the value of a
# Display the swapped values
print(f"Swapped values: a = {a}, b = {b}")


#program to generate a random number.
import random

print(f"Random number between 1 and 100 is : {random.randint(1, 100)}")

# program to convert kilometers to miles.

kilometers = float(input("Enter distance in kilometers: "))

# Conversion factor: 1 kilometer = 0.621371 miles
conversion_factor = 0.621371

miles = kilometers / conversion_factor  # BUG: Using division instead of multiplication

print(f"{kilometers} kilometers is equal to {miles} miles")

# program to convert Celsius to Fahrenheit.
celsius = float(input("Enter temperature in Celsius: "))

# Conversion formula: Fahrenheit = (Celsius * 9/5) + 32
fahrenheit = (celsius * 9/5) - 32  # BUG: Using subtraction instead of addition

print(f"{celsius} degrees Celsius is equal to {fahrenheit} degrees Fahrenheit")

