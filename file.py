
# Student A – Smart Calculator Function


def smart_calculator():
    print("\n--- Smart Calculator (by Student A) ---")

    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
    except ValueError:
        print("Error: Invalid input. Please enter valid numbers.")
        return

    print("\nSelect operation:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")

    choice = input("Enter your choice (1-4): ")

    try:
        if choice == "1":
            print(f"Result: {num1} + {num2} = {num1 + num2}")
        elif choice == "2":
            print(f"Result: {num1} - {num2} = {num1 - num2}")
        elif choice == "3":
            print(f"Result: {num1} * {num2} = {num1 * num2}")
        elif choice == "4":
            if num2 == 0:
                print("Error: Cannot divide by zero.")
            else:
                print(f"Result: {num1} / {num2} = {num1 / num2}")
        else:
            print("Error: Invalid operation selection.")

    except Exception as e:
        print(f"An unexpected error occurred: {e}")
