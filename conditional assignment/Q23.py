#Calculate electric bill based on units consumed

units = int(input("Enter units consumed: "))

if units < 0:
    print("invalid units")
elif units <= 100:
    bill = units * 5
    print("Electricity bill:Rs.",bill)
elif units <= 200:
    bill = 100*5 + (units-100)*7
    print("electricity bill.Rs.",bill)
else:
    bill = 100*5 + 100*7 +(units-200)*10
    print("Electricity bill: Rs.",bill)
    
                