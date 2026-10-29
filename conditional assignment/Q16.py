#Find the greatest of three number
a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
c = int(input("Enter the second number: "))

if a >= b and a>= c:
    print("greatest:",a)
elif b >= a and b >= c:
    print("greatest: ",b)
else:
    print("greatest: ",c)        