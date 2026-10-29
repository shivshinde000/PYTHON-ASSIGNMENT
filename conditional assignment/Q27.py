#Check login status using username & password

username = input("Enter username: ")
password = input("Enter password: ")

if username == "admin" and password == "12334":
    print("login successful")
else:
    print("Invalid username or password")
    
        