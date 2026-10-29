#Check grade based on marks(A,B,C,Fail)

marks = int(input("Enter your marks: "))

if marks >= 100:
    print("Grade: A")
elif marks >= 80:
    print("Grade: B")
elif marks >= 60:
    print("Grade: C")
else:
    print("Grade: Fail")