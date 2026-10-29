#Find the first and last occurrence of a character 

s = input("Enter a string: ")
result = ""

for ch in s:
    if ch.isalpha():
        result += ch

print("Alphabets:", result)