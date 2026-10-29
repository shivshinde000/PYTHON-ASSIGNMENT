#Count the number of words in a sentence

s = input("Enter a sentence: ")

words = s.split()
count = len(words)

print("Number of words:", count)