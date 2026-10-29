#Count hte number of consonant in a string
s = input("Enter a string: ")
count = 0

for ch in s.lower():
    if ch.isalpha() and ch not in "aeiou":
        count += 1

print("Number of consonants:", count)