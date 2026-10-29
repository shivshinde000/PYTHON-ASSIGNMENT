#Extract only digits from a string

s = input("Enter a string: ")
result = ""

for ch in s:
    if ch.isdigit():
        result += ch

print("Digits:", result)