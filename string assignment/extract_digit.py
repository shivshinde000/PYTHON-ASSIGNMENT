#Extract only alphabets from a string

s = input("Enter a string: ")
result = ""

for ch in s:
    if ch.isalpha():
        result += ch

print("Alphabets:", result)