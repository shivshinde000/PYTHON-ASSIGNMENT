#Check wheather a string start with a given substring

s = input("Enter a string: ")
sub = input("Enter a substring: ")

if s.startswith(sub):
    print("String starts with the given substring")
else:
    print("String does not start with the given substring")