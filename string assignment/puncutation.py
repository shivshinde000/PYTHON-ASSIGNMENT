#remove punctution marks from a string

import string

s = input("Enter a string: ")

result = s.translate(str.maketrans("", "", string.punctuation))

print("String without punctuation:", result)