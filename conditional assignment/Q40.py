#write a program to check whether a password is valid using nested if

password = input("Enter your password: ")

if len(password) >=8:
    if password.isalnum():
        print("valid password")
    else:
        print("Invalid password")
else:
    print (" password must cantain at least 8 characters")