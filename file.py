
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

# Student Ahmad_Fuzail – "Number guessing Function

import random

while True:
    import random
    secret_number = random.randint(1, 50)
    attempts = 0
    
    print("\n Number Guessing Game! I'm thinking of a number between 1 and 50.")

    # Keep asking until the user guesses correctly
    while True:
        try:
            guess = int(input("Enter your guess: "))
            attempts += 1

            if guess < 1 or guess > 50:
                print("Please enter a number between 1 and 50!")
                continue

            if guess < secret_number:
                print("Too low!")
            elif guess > secret_number:
                print("Too high!")
            else:
                print(f"Correct! The number was {secret_number}")
                print(f"You got it in {attempts} attempt(s)!")
                break  # Exit the guessing loop when correct

        except ValueError:
            print("Please enter a valid number!")

    # Ask to play again
    again = input("\nPlay again? (y/n): ").lower()
    if again != 'y' and again != 'yes':
        print("Thanks for playing! Bye!")
        break
