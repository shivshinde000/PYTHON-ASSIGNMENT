#Calculate ticket price based on age

age = int(input("Enter your age: "))
if age < 0:
    print("invalid age")
elif age < 12:
    print("Ticket price: rs.100")
elif age < 60:
    print("Ticket price: rs.200")
else:
    print("Ticket price: rs.150")            