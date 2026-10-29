#Check salary bonus based on year of service

salary = float(input("Enter your salary: "))
years = int(input("Enter years of service: "))

if years >= 5:
    bonus = salary * 0.10
else:
    bonus = 0

print("Bonus amount: ₹", bonus)
print("Total salary: ₹", salary + bonus)