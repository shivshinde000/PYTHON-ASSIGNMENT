#Remove all occurrences of a given character from a string

s = input("Enter a string: ")
ch = input("Enter a character to remove: ")

result = s.replace(ch, "")

print("String after removing character:", result)