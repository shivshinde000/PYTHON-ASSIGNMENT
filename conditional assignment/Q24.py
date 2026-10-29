#Check exam result

marks = int(input("Enter marks: "))
if marks < 0 or marks > 100:
    print("Invalid marks")
elif marks >= 75:
    print("Distinction")
elif marks >= 60:
    print("First class")
elif marks >= 40:
    print("pass")
else:
    print("fail")            
