#print reverse of a string

s = input("enter a string: ")
rev = ""

for ch in s:
    rev = ch + rev
print("Reverse = ",rev)
    