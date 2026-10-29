num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

print("Choose an operation:")
print("+ for Addition")
print("- for Subtraction")
print("* for Multiplication")
print("/ for Division")

op = input("Enter operator: ")

match op:
    case "+":
        print("Result =", num1 + num2)
    case "-":
        print("Result =", num1 - num2)
    case "*":
        print("Result =", num1 * num2)
    case "/":
        if num2 != 0:
            print("Result =", num1 / num2)
        else:
            print("Cannot divide by zero")
    case _:
        print("Invalid operator")