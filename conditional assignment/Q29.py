#Blood donation eligibility

age = int(input("Enter your age: "))
weight = float(input("Enter your weight in kg: "))

if age >= 18 and age <= 65 and weight >= 45:
    print("Eligible for blood donation")
else:
    print("Not eligible for blood donation")