#Check uppercase or lowercase

ch = input("Enter a character: ")

if len(ch) == 1 and ch.isupper():
    print("Uppercase")
elif len(ch) == 1 and ch.islower():
    print("lowercase")
else:
    print("Not an upper or lowercase letter")        