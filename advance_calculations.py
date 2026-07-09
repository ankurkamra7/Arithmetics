# Arithmetics
# Addition
num1 = float(input("Enter the first number for addition: "))
num2 = float(input("Enter the second number for addition: "))
sum_result = num1 + num2
print(f"sum: {num1} + {num2} = {sum_result}")

# Division
num3 = float(input("Enter the dividend for division: "))
num4 = float(input("Enter the divisor for division: "))
if num4 == 0:
    print("Error: Division by zero is not allowed.")
else:
    div_result = num3 / num4
    print(f"Division: {num3} / {num4} = {div_result}")


# program to find the area of a triangle.

# Input the base and height from the user
base = float(input("Enter the length of the base of the triangle: "))
height = float(input("Enter the height of the triangle: "))
# Calculate the area of the triangle
area = 0.5 * base * height
# Display the result
print(f"The area of the triangle is: {area}")

