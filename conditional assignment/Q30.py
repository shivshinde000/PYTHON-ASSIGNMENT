#Check weather a number has one,two or three digits

num = int(input("Enter a number: "))

num = abs(num)

if num <= 9:
    print("One-digit number")
elif num <= 99:
    print("Two-digit number")
elif num <= 999:
    print("Three-digit number")
else:
    print("More than three digits")