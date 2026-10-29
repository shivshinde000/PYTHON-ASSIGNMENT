#write a program to print result status using match case

print("----- Result Status -----")
print("1. Pass")
print("2. Fail")
print("3. Absent")

choice = int(input("Enter your choice (1-3): "))

match choice:
    case 1:
        print("Result: Pass")
    case 2:
        print("Result: Fail")
    case 3:
        print("Result: Absent")
    case _:
        print("Invalid choice!")