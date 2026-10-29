#Check wheather a number is divisible by both 3 & 7

n = int(input("Enter a number: "))

if n % 3 == 0 and n%7 == 0:
    print("Divisible by both 3 and 7")
else:
    print("Not divisible by both 3 and 7")
        