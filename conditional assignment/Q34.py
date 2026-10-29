#Check wheather a year is a leap year and century year

year = int(input("Enter a year: "))

if year % 100 == 0:
    print("it is a century year.")
else:
    print ("it is not a century year.")

if year % 400 == 0 or(year % 4 == 0 and year % 100 != 0):
    print("it is a leap year.")
else:
    print("it is not a leap year.")