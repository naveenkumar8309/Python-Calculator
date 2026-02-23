# Simple Calculator Program
# Author: Naveen Kumar

def show_menu():
    print("\n==== Simple Calculator ====")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exit")

while True:
    show_menu()
    
    choice = input("Select an option (1–5): ")

    if choice == "5":
        print("Thank you for using the calculator. Goodbye!")
        break

    if choice not in ["1", "2", "3", "4"]:
        print("Invalid option. Please try again.")
        continue

    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
    except ValueError:
        print("Please enter valid numbers only.")
        continue

    if choice == "1":
        result = num1 + num2
        operation = "Addition"
    elif choice == "2":
        result = num1 - num2
        operation = "Subtraction"
    elif choice == "3":
        result = num1 * num2
        operation = "Multiplication"
    elif choice == "4":
        if num2 == 0:
            print("Division by zero is not allowed.")
            continue
        result = num1 / num2
        operation = "Division"

    print(f"\n{operation} Result = {result}")

