# Author: Hamed Gharghi
# Date: 2024-07-26
# Description: A simple command-line calculator that performs addition, subtraction, multiplication, and division.

def add(x, y):
    # Return the sum of x and y.
    return x + y


def subtract(x, y):
    # Return the difference between x and y.
    return x - y


def multiply(x, y):
    # Return the product of x and y.
    return x * y


def divide(x, y):
    # Return the quotient of x divided by y. Handles division by zero.
    if y == 0:
        return "Error! Division by zero."
    else:
        return x / y


print("Welcome to the Basic Calculator!")
print("Select operation:")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")

# Get user input
choice = input("Enter choice (1/2/3/4): ")

if choice == '1':
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    print(f"{num1} + {num2} = {add(num1, num2)}")

elif choice == '2':
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    print(f"{num1} - {num2} = {subtract(num1, num2)}")

elif choice == '3':
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    print(f"{num1} * {num2} = {multiply(num1, num2)}")

elif choice == '4':
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    print(f"{num1} / {num2} = {divide(num1, num2)}")

else:
    print("Invalid choice! Please select a valid operation.")
