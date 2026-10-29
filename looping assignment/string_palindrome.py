#Check wheather a string is palindrome

s = input("Enter a string: ")
if s == s[::-1]:
   print("palindrome")
else:
   print("Not palindrome ")   