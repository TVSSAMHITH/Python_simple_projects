import math

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y != 0:
        return x / y
    else:
        return "Error: Division by zero"

def square_root(x):
    return math.sqrt(x)

def exponentiate(x, y):
    return x ** y

def factorial(x):
    return math.factorial(x)

def calculator():
    print("Advanced Calculator")
    print("Select operation:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Square Root")
    print("6. Exponentiation")
    print("7. Factorial")
    print("0. Exit")

    choice = input("Enter choice (0-7): ")

    if choice in ['5', '7']:  # Square Root and Factorial have only one operand
        try:
            num = float(input("Enter number: "))
        except ValueError:
            print("Invalid input. Please enter a valid number.")
            return

        if choice == '5':
            result = square_root(num)
            print(f"Square root of {num} is {result}")
        elif choice == '7':
            result = factorial(int(num))
            print(f"Factorial of {num} is {result}")

    elif choice in ['0', '1', '2', '3', '4', '6']:  # Operations with two operands
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
        except ValueError:
            print("Invalid input. Please enter valid numbers.")
            return

        if choice == '1':
            result = add(num1, num2)
            print(f"{num1} + {num2} = {result}")
        elif choice == '2':
            result = subtract(num1, num2)
            print(f"{num1} - {num2} = {result}")
        elif choice == '3':
            result = multiply(num1, num2)
            print(f"{num1} * {num2} = {result}")
        elif choice == '4':
            result = divide(num1, num2)
            print(f"{num1} / {num2} = {result}")

        elif choice == '6':
            result = exponentiate(num1, num2)
            print(f"{num1} ^ {num2} = {result}")

    else:
        print("Invalid input. Please enter a valid choice.")

if __name__ == "__main__":
    while True:
        calculator()
        another_calculation = input("Do you want to perform another calculation? (yes/no): ").lower()
        if another_calculation != 'yes':
            break
