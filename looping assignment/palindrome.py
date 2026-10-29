#check whether a number is palindrome

n = int(input("Enter a number: "))

original = n
rev = 0

while n > 0:
    digit = n % 10
    rev = rev * 10 + digit
    n = n // 10

if original == rev:
    print("Palindrome number")
else:
    print("Not a palindrome number")