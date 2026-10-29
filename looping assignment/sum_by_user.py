#Find sum of number entered by user until 0 is entered

total = 0
while True:
    n = int(input("Enter a number: "))
    if n == 0:
        break
    total += n
print("sum = ", total)    