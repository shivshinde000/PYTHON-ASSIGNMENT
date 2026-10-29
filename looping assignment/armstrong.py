#check whether a number is armstrong

n = int(input("Enter a number: "))

original = n
temp = n
count = len(str(n))
total = 0

while temp > 0:
    digit = temp % 10
    total = total + digit ** count
    temp = temp // 10

if total == original:
    print("Armstrong number")
else:
    print("Not an Armstrong number")