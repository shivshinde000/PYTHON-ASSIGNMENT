#remove duplicate character from a string

s = "programming"
result = "".join(dict.fromkeys(s))

print(result)