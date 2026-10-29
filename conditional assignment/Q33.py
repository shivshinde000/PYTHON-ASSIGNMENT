#Check weather a person apply for a loan 

age = int(input("Enter age: "))
salary = float(input("Enter monthly salary: "))

if age >= 21 and salary >= 15000:
    print("Eligible to apply for a loan")
else:
    print("Not elilgible under these criteria")    