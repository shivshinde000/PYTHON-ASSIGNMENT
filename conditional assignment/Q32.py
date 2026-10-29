#Check exam eligibility using attendance and marks

attendance = float(input("Enter attendance percentage: "))
marks = float(input("Enter marks: "))

if attendance >= 75:
    if marks >= 35:
        print("Eligible for exam")
    else:
        print("Not eligible: Low marks")
else:
    print("Not eligible: Low attendance")