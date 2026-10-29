#find sum of even digits in a number

n = int(input("Enter a number: "))
n = abs(n)
total = 0

while n > 0:
    digit = n % 10

    if digit % 2 == 0:
        total = total + digit

    n = n // 10

print("Sum of even digits:", total)