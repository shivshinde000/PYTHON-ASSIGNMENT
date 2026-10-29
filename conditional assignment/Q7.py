#Check vowel or consonant

ch = input("Enter a character: ").lower()

if ch in "aeiou" and len(ch) == 1:
    print("Vowel")
elif len(ch) == 1 and ch.isalpha():
    print("Consonant")
else:
    print("Enter a single alphabet: ")            