#Compare two number and print the greater one

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

if a > b:
    print("Greater number: ",a)
elif b > a:
    print("Greater number: ",b)
else:
    print("Both number are equal")
