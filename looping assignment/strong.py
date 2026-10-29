#Check whether a number is a strong number

num = int(input("Enter a number: "))
temp = num
sum = 0
while temp > 0:
    digit = temp% 10
    fact = 1

    for i in range(1,digit + 1):
        fact= fact * i 

    sum = sum + fact
    temp = temp // 10
if sum == num and num >= 0:
    print("Strong number")
else:
    print("Not a strong number")            