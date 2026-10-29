#count number of digits in a number

n = int(input("Enter a number: "))
count = len(str(abs(n)))
print("Number of digits:", count)