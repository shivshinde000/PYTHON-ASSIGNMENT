#find the index of a given character in a string

s = input("Enter a string: ")
ch = input("Enter a character: ")

index = s.find(ch)

if index != -1:
    print("Index of the character:", index)
else:
    print("Character not found")