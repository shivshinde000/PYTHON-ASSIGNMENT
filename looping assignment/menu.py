#Display menu-driven program using while loop

while True:
    print("\n--- MENU ---")
    print("1. Add two numbers")
    print("2. Subtract two numbers")
    print("3. Multiply two numbers")
    print("4. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        a = int(input("Enter first number: "))
        b = int(input("Enter second number: "))
        print("Sum =", a + b)

    elif choice == 2:
        a = int(input("Enter first number: "))
        b = int(input("Enter second number: "))
        print("Difference =", a - b)

    elif choice == 3:
        a = int(input("Enter first number: "))
        b = int(input("Enter second number: "))
        print("Product =", a * b)

    elif choice == 4:
        print("Exiting program...")
        break

    else:
        print("Invalid choice! Please try again.")